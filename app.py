from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from core.ai_assistant import generate_product_questions
from core.content import build_decision_memo, build_prd
from core.decision_engine import GATES, Gate, decision, risk_level, risk_rows
from core.risk_register import clone_seed_risks, clean_risk_records, risk_objects
from core.workspace import (
    DEMO_BRIEF,
    brief_to_dict,
    clone_seed_evals,
    evaluation_summary,
    sanitize_brief,
    sanitize_evals,
)

ROOT = Path(__file__).parent
st.set_page_config(page_title="LaunchPilot AI", page_icon="🚀", layout="wide")


# -----------------------------------------------------------------------------
# Session state: every editable object has its own stable namespace/key.
# Streamlit reruns the script after interaction, so all product state lives here.
# -----------------------------------------------------------------------------
def init_state() -> None:
    defaults = {
        "brief": brief_to_dict(DEMO_BRIEF),
        "risks": clone_seed_risks(),
        "evals": clone_seed_evals(),
        "gate_scores": [82, 88, 91, 78, 76],
        "gate_evidence": ["Customer interviews + prototype evidence", "Offline eval set + failure review", "Safety review + escalation policy", "Monitoring + rollback plan", "Controlled beta business case"],
        "gate_version": 0,
        "risk_counter": 100,
        "brief_version": 0,
        "eval_version": 0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_all() -> None:
    st.session_state.brief = brief_to_dict(DEMO_BRIEF)
    st.session_state.risks = clone_seed_risks()
    st.session_state.evals = clone_seed_evals()
    st.session_state.gate_scores = [82, 88, 91, 78, 76]
    st.session_state.gate_evidence = ["Customer interviews + prototype evidence", "Offline eval set + failure review", "Safety review + escalation policy", "Monitoring + rollback plan", "Controlled beta business case"]
    st.session_state.gate_version += 1
    st.session_state.brief_version += 1
    st.session_state.eval_version += 1
    st.rerun()


init_state()


@st.cache_data
def load_demo():
    with open(ROOT / "data" / "demo_product.json", encoding="utf-8") as f:
        product = json.load(f)
    return product


# -----------------------------------------------------------------------------
# Sidebar
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("LaunchPilot AI")
    st.caption("AI Product Launch & Decision OS")
    if st.button("Reset entire workspace", use_container_width=True):
        reset_all()
    st.divider()
    st.markdown("**Portfolio mode**")
    st.caption("Deterministic demo. No API key required.")
    st.caption("All demo outcomes are synthetic and illustrative.")

p = st.session_state.brief

st.title("🚀 LaunchPilot AI")
st.caption("Evidence-led product discovery, evaluation, risk management and launch decisioning.")

cols = st.columns(4)
cols[0].metric("Product", p["name"])
cols[1].metric("Category", p["category"])
cols[2].metric("Launch gates", "5")
summary = evaluation_summary(st.session_state.evals)
cols[3].metric("AI eval", summary["status"])

st.info(f"**Problem:** {p['problem']}\n\n**Promise:** {p['promise']}")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1 · Product Brief",
    "2 · 5-Gate Review",
    "3 · Risk & Trust",
    "4 · AI Evaluation",
    "5 · Executive Decision",
])

# -----------------------------------------------------------------------------
# 1. Product Brief — independent form state
# -----------------------------------------------------------------------------
with tab1:
    st.subheader("Product Brief")
    st.caption("Edit the product definition independently, then save it. Downstream gates and the executive memo use the saved brief.")
    with st.form(f"brief_form_{st.session_state.brief_version}"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Product name", p["name"])
            category = st.text_input("Category", p["category"])
            problem = st.text_area("Customer problem", p["problem"], height=120)
            persona = st.text_area("Target user", p["persona"], height=100)
            promise = st.text_area("Product promise", p["promise"], height=100)
        with c2:
            mvp = st.text_area("MVP scope", p["mvp"], height=120)
            non_goals = st.text_area("Non-goals", p["non_goals"], height=100)
            north_star = st.text_area("North Star Metric", p["north_star"], height=100)
            success_targets = st.text_area("Success targets", p["success_targets"], height=100)
        save_brief = st.form_submit_button("Save Product Brief", type="primary", use_container_width=True)

    if save_brief:
        st.session_state.brief = sanitize_brief({
            "name": name, "category": category, "problem": problem, "persona": persona,
            "promise": promise, "mvp": mvp, "non_goals": non_goals,
            "north_star": north_star, "success_targets": success_targets,
        })
        st.session_state.brief_version += 1
        st.success("Product Brief saved. Only the brief changed; other workspace sections were preserved.")
        st.rerun()

    st.markdown("### Product snapshot")
    st.dataframe(
        pd.DataFrame([
            {"Field": "Product", "Value": p["name"]},
            {"Field": "Category", "Value": p["category"]},
            {"Field": "Target user", "Value": p["persona"]},
            {"Field": "Customer problem", "Value": p["problem"]},
            {"Field": "Product promise", "Value": p["promise"]},
            {"Field": "MVP scope", "Value": p["mvp"]},
            {"Field": "North Star Metric", "Value": p["north_star"]},
            {"Field": "Success targets", "Value": p["success_targets"]},
        ]),
        use_container_width=True,
        hide_index=True,
    )
    st.download_button("Download AI PRD", build_prd(p), file_name="AI_PRD.md", mime="text/markdown", use_container_width=True)
    st.subheader("PM discovery questions")
    for question in generate_product_questions(p["problem"], p["persona"]):
        st.write("• " + question)

# -----------------------------------------------------------------------------
# 2. 5-Gate Review — one unique widget key per gate
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("5-Gate Launch Readiness")
    st.caption("Each gate has independent score and evidence state. Changes to one gate never overwrite another gate.")

    with st.form(f"gates_form_{st.session_state.gate_version}"):
        new_scores = []
        new_evidence = []
        for i, gate_name in enumerate(GATES):
            st.markdown(f"### {i + 1}. {gate_name}")
            c1, c2 = st.columns([1, 2])
            with c1:
                new_scores.append(st.slider("Score", 0, 100, int(st.session_state.gate_scores[i]), key=f"gate_score_{st.session_state.gate_version}_{i}"))
            with c2:
                new_evidence.append(st.text_input("Evidence", st.session_state.gate_evidence[i], key=f"gate_evidence_{st.session_state.gate_version}_{i}"))
        save_gates = st.form_submit_button("Save Gate Review", type="primary", use_container_width=True)

    if save_gates:
        st.session_state.gate_scores = list(new_scores)
        st.session_state.gate_evidence = list(new_evidence)
        st.success("Gate Review saved. Each gate remains independently editable.")
        st.rerun()

    gates = [Gate(name, st.session_state.gate_scores[i], threshold=70, critical=(name in {"AI Quality", "Trust & Safety"}), evidence=st.session_state.gate_evidence[i]) for i, name in enumerate(GATES)]
    current_risks = risk_objects(st.session_state.risks)
    result = decision(gates, current_risks, business_target_met=True)
    st.dataframe(pd.DataFrame([
        {"Gate": g.name, "Score": g.score, "Threshold": g.threshold, "Status": "PASS" if g.passed else "FAIL", "Critical": "Yes" if g.critical else "No", "Evidence": g.evidence}
        for g in gates
    ]), use_container_width=True, hide_index=True)
    fig = px.bar(pd.DataFrame({"Gate": GATES, "Score": st.session_state.gate_scores}), x="Gate", y="Score", range_y=[0, 100], title="Launch gate readiness")
    fig.add_hline(y=70, line_dash="dash", annotation_text="Threshold")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------
# 3. Risk & Trust — stable IDs + one form per risk; no shared editor state
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("Trust, Safety & Operational Risk Register")
    st.caption("Every risk is an independent record. Edit, save, add or delete one risk without changing any other risk.")

    c1, c2 = st.columns([1, 3])
    with c1:
        if st.button("Reset demo risks", use_container_width=True):
            st.session_state.risks = clone_seed_risks()
            st.success("Demo risks restored.")
            st.rerun()
    with c2:
        st.info("Exposure = Likelihood × Impact. Critical ≥16 · High 9–15 · Medium 4–8 · Low <4")

    # Add-risk form is separate from existing risk forms.
    with st.expander("➕ Add a new risk", expanded=False):
        with st.form("add_risk_form"):
            c1, c2 = st.columns(2)
            with c1:
                new_title = st.text_input("Risk title", key="add_risk_title")
                new_category = st.text_input("Category", "Operations", key="add_risk_category")
                new_owner = st.text_input("Owner", "Product", key="add_risk_owner")
            with c2:
                new_likelihood = st.selectbox("Likelihood", [1, 2, 3, 4, 5], index=2, key="add_risk_likelihood")
                new_impact = st.selectbox("Impact", [1, 2, 3, 4, 5], index=2, key="add_risk_impact")
                new_mitigation = st.text_area("Mitigation", "Define a preventive or detective control.", key="add_risk_mitigation")
            add_risk = st.form_submit_button("Add Risk", type="primary")
        if add_risk:
            title = new_title.strip()
            if not title:
                st.error("Risk title is required.")
            else:
                st.session_state.risk_counter += 1
                record = {"id": f"risk-{st.session_state.risk_counter}", "title": title, "category": new_category.strip() or "Operations", "likelihood": int(new_likelihood), "impact": int(new_impact), "mitigation": new_mitigation.strip(), "owner": new_owner.strip() or "Product"}
                st.session_state.risks.append(record)
                st.success(f"Added: {title}")
                st.rerun()

    if not st.session_state.risks:
        st.warning("No risks defined. Add a risk above.")

    for index, risk in enumerate(list(st.session_state.risks)):
        risk_id = risk.get("id") or f"risk-{index}"
        risk["id"] = risk_id
        exposure = int(risk["likelihood"]) * int(risk["impact"])
        label = f"{risk['title']} · {risk_level(exposure)} ({exposure})"
        with st.expander(label, expanded=(index == 0)):
            with st.form(f"risk_form_{risk_id}"):
                c1, c2, c3 = st.columns([2, 1, 1])
                with c1:
                    title = st.text_input("Risk", risk["title"], key=f"risk_title_{risk_id}")
                    mitigation = st.text_area("Mitigation", risk["mitigation"], key=f"risk_mitigation_{risk_id}")
                with c2:
                    category = st.text_input("Category", risk["category"], key=f"risk_category_{risk_id}")
                    likelihood = st.selectbox("Likelihood", [1, 2, 3, 4, 5], index=int(risk["likelihood"]) - 1, key=f"risk_likelihood_{risk_id}")
                with c3:
                    owner = st.text_input("Owner", risk["owner"], key=f"risk_owner_{risk_id}")
                    impact = st.selectbox("Impact", [1, 2, 3, 4, 5], index=int(risk["impact"]) - 1, key=f"risk_impact_{risk_id}")
                save_risk = st.form_submit_button("Save this risk", type="primary")
            if save_risk:
                updated = {"id": risk_id, "title": title, "category": category, "likelihood": likelihood, "impact": impact, "mitigation": mitigation, "owner": owner}
                cleaned = clean_risk_records([updated])[0]
                cleaned["id"] = risk_id
                for j, existing in enumerate(st.session_state.risks):
                    if existing.get("id") == risk_id:
                        st.session_state.risks[j] = cleaned
                        break
                st.success(f"Saved only: {cleaned['title']}")
                st.rerun()
            if st.button("Delete this risk", key=f"delete_{risk_id}", type="secondary"):
                st.session_state.risks = [r for r in st.session_state.risks if r.get("id") != risk_id]
                st.rerun()

    current_risks = risk_objects(st.session_state.risks)
    rdf = pd.DataFrame(risk_rows(current_risks))
    st.markdown("### Calculated risk exposure")
    st.dataframe(rdf, use_container_width=True, hide_index=True)
    if not rdf.empty:
        fig = px.scatter(rdf, x="likelihood", y="impact", size="Exposure", text="title", hover_name="title", range_x=[0, 6], range_y=[0, 6], title="Risk exposure map")
        fig.update_traces(textposition="top center")
        st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------
# 4. AI Evaluation — independent editable evaluation cases and live summary
# -----------------------------------------------------------------------------
with tab4:
    st.subheader("AI Evaluation Workbench")
    st.caption("Edit each evaluation case independently. The aggregate quality/safety score is recalculated from the saved cases.")

    with st.form(f"eval_form_{st.session_state.eval_version}"):
        updated_evals = []
        for i, case in enumerate(st.session_state.evals):
            st.markdown(f"### Evaluation Case {i + 1}")
            c1, c2 = st.columns([2, 1])
            with c1:
                case_text = st.text_input("Test case", case["case"], key=f"eval_case_{st.session_state.eval_version}_{i}")
                expected = st.text_input("Expected behavior", case["expected"], key=f"eval_expected_{st.session_state.eval_version}_{i}")
            with c2:
                quality = st.slider("Quality", 0, 100, int(case["quality"]), key=f"eval_quality_{st.session_state.eval_version}_{i}")
                safety = st.slider("Safety", 0, 100, int(case["safety"]), key=f"eval_safety_{st.session_state.eval_version}_{i}")
            updated_evals.append({"id": case["id"], "case": case_text, "expected": expected, "quality": quality, "safety": safety})
        save_evals = st.form_submit_button("Save Evaluation Set", type="primary", use_container_width=True)

    if save_evals:
        st.session_state.evals = sanitize_evals(updated_evals)
        st.session_state.eval_version += 1
        st.success("Evaluation set saved. Each case is independent.")
        st.rerun()

    summary = evaluation_summary(st.session_state.evals)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Average quality", f"{summary['quality']}%")
    c2.metric("Average safety", f"{summary['safety']}%")
    c3.metric("Case pass rate", f"{summary['pass_rate']}%")
    if summary["status"] == "PASS":
        c4.success("PASS")
    else:
        c4.warning("ITERATE")

    eval_df = pd.DataFrame(st.session_state.evals)
    st.dataframe(eval_df[["case", "expected", "quality", "safety"]], use_container_width=True, hide_index=True)
    st.download_button("Download evaluation cases", eval_df.to_csv(index=False), file_name="ai_eval_cases.csv", mime="text/csv", use_container_width=True)

# -----------------------------------------------------------------------------
# 5. Executive Decision — read-only synthesis of the current saved workspace
# -----------------------------------------------------------------------------
with tab5:
    st.subheader("Executive Launch Decision")
    st.caption("This page intentionally has no duplicate editable controls. It is a synthesis of the saved Product Brief, Gate Review, Risk Register and AI Evaluation state.")

    gates = [Gate(name, st.session_state.gate_scores[i], threshold=70, critical=(name in {"AI Quality", "Trust & Safety"}), evidence=st.session_state.gate_evidence[i]) for i, name in enumerate(GATES)]
    current_risks = risk_objects(st.session_state.risks)
    eval_summary = evaluation_summary(st.session_state.evals)

    # AI Evaluation is a launch input: critical safety quality below threshold is a blocker.
    eval_blocker = eval_summary["safety"] < 90 or eval_summary["quality"] < 80 or eval_summary["pass_rate"] < 80
    blockers = ["AI Evaluation threshold not met"] if eval_blocker else []
    result = decision(gates, current_risks, business_target_met=not eval_blocker, critical_blockers=blockers)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Decision", result["verdict"])
    c2.metric("Readiness", f"{result['overall_score']}/100")
    c3.metric("Gate pass rate", f"{result['gate_pass_rate']}%")
    c4.metric("AI evaluation", eval_summary["status"])

    if result["verdict"] == "GO":
        st.success(f"GO — readiness score {result['overall_score']}/100")
    elif result["verdict"] == "ITERATE":
        st.warning(f"ITERATE — readiness score {result['overall_score']}/100")
    else:
        st.error(f"NO-GO — readiness score {result['overall_score']}/100")

    st.write(result["rationale"])
    if eval_blocker:
        st.error("AI evaluation is below the controlled-rollout threshold. Improve evaluation quality/safety before launch.")
    if result["critical_risks"]:
        st.error("Critical risks blocking launch: " + ", ".join(result["critical_risks"]))
    elif result["high_risks"]:
        st.warning("High risks requiring iteration: " + ", ".join(result["high_risks"]))
    else:
        st.success("No high-severity risk is currently blocking the decision.")

    # -------------------------------------------------------------------------
    # Executive evidence tables
    # -------------------------------------------------------------------------
    st.markdown("## Executive evidence summary")
    st.caption("This is the single-page PM view of the saved workspace. It intentionally contains read-only tables so a recruiter can see the evidence behind the decision without navigating between tabs.")

    st.markdown("### 1. Product Brief")
    brief_df = pd.DataFrame([
        {"Field": "Product", "Value": p["name"]},
        {"Field": "Category", "Value": p["category"]},
        {"Field": "Target user", "Value": p["persona"]},
        {"Field": "Customer problem", "Value": p["problem"]},
        {"Field": "Product promise", "Value": p["promise"]},
        {"Field": "MVP scope", "Value": p["mvp"]},
        {"Field": "North Star Metric", "Value": p["north_star"]},
        {"Field": "Success targets", "Value": p["success_targets"]},
    ])
    st.dataframe(brief_df, use_container_width=True, hide_index=True)

    st.markdown("### 2. 5-Gate Review")
    gate_df = pd.DataFrame([
        {
            "Gate": g.name,
            "Score": g.score,
            "Threshold": g.threshold,
            "Status": "PASS" if g.passed else "FAIL",
            "Critical": "Yes" if g.critical else "No",
            "Evidence": g.evidence,
        }
        for g in gates
    ])
    st.dataframe(gate_df, use_container_width=True, hide_index=True)

    st.markdown("### 3. Risk & Trust")
    risk_df = pd.DataFrame(risk_rows(current_risks))
    if risk_df.empty:
        st.info("No risks are currently registered.")
    else:
        risk_view = risk_df.rename(columns={
            "title": "Risk",
            "category": "Category",
            "likelihood": "Likelihood",
            "impact": "Impact",
            "Exposure": "Exposure",
            "Level": "Level",
            "mitigation": "Mitigation",
            "owner": "Owner",
        })[["Risk", "Category", "Likelihood", "Impact", "Exposure", "Level", "Owner", "Mitigation"]]
        st.dataframe(risk_view, use_container_width=True, hide_index=True)

    st.markdown("### 4. AI Evaluation")
    eval_df = pd.DataFrame(st.session_state.evals)
    if eval_df.empty:
        st.info("No AI evaluation cases are currently defined.")
    else:
        eval_view = eval_df[["case", "expected", "quality", "safety"]].rename(columns={
            "case": "Test case",
            "expected": "Expected behavior",
            "quality": "Quality",
            "safety": "Safety",
        })
        st.dataframe(eval_view, use_container_width=True, hide_index=True)

    st.markdown("### 5. Decision Summary")
    decision_df = pd.DataFrame([
        {"Decision metric": "Final verdict", "Value": result["verdict"]},
        {"Decision metric": "Overall readiness", "Value": f'{result["overall_score"]}/100'},
        {"Decision metric": "Gate pass rate", "Value": f'{result["gate_pass_rate"]}%'},
        {"Decision metric": "AI evaluation", "Value": eval_summary["status"]},
        {"Decision metric": "AI quality", "Value": f'{eval_summary["quality"]}%'},
        {"Decision metric": "AI safety", "Value": f'{eval_summary["safety"]}%'},
        {"Decision metric": "Evaluation pass rate", "Value": f'{eval_summary["pass_rate"]}%'},
        {"Decision metric": "Critical risks", "Value": len(result["critical_risks"])},
        {"Decision metric": "High risks", "Value": len(result["high_risks"])},
        {"Decision metric": "Failed gates", "Value": len(result["failed_gates"])},
    ])
    st.dataframe(decision_df, use_container_width=True, hide_index=True)

    next_steps = [
        "Run a controlled beta with a defined support-team cohort.",
        "Review severe AI failures weekly and re-evaluate the launch scorecard.",
        "Monitor resolution rate, CSAT, escalation rate and policy-groundedness.",
        "Scale only after guardrails remain stable for two consecutive review cycles.",
    ]
    st.markdown("**Recommended next actions**")
    for step in next_steps:
        st.write("• " + step)
    st.download_button("Download executive decision memo", build_decision_memo(p, result, next_steps), file_name="Executive_Launch_Decision.md", mime="text/markdown", use_container_width=True)

st.divider()
st.caption("LaunchPilot AI is a portfolio/learning product. Demo data and outcomes are synthetic; readiness scores are illustrative targets, not real customer results.")
