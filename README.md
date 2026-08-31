# 🚀 LaunchPilot AI

**AI Product Launch & Decision OS** for evidence-led product discovery, AI evaluation, trust & safety, launch readiness, and executive decision-making.

> Portfolio project for Product Management. Demo data and outcomes are synthetic and illustrative.

## 🚀 Live Demo

[LaunchPilot AI — Live Demo](https://launchpilot-ai-abhi-iitg.streamlit.app/)

## 🎯 Executive Decision Dashboard

![LaunchPilot AI — Executive Decision Dashboard](screenshots/05-executive-decision.png)

## 🎥 Product Demo

Interactive AI product launch decision platform demonstrating:

- Product Brief
- 5-Gate Launch Review
- Risk & Trust Management
- AI Evaluation
- Executive GO / ITERATE / NO-GO Decision

## Live product workflow

**Product Brief → 5-Gate Review → Risk & Trust → AI Evaluation → Executive Decision**

## 🧠 PM Capabilities Demonstrated

| PM Capability | Demonstrated Through |
|---|---|
| Product Discovery | Problem definition, target user, product promise |
| PRD Development | Product Brief and MVP scope |
| Product Strategy | Product goals, North Star Metric and success criteria |
| AI Product Management | AI evaluation and quality thresholds |
| Responsible AI | Trust & Safety assessment |
| Risk Management | Likelihood × Impact risk framework |
| Product Analytics | Readiness metrics and evaluation metrics |
| Experimentation | AI evaluation cases and launch criteria |
| GTM | Launch and rollout planning |
| Executive Communication | Executive Decision Memo |
| Decision Making | GO / ITERATE / NO-GO framework |

## Key product features

### 1 · Product Brief
Edit and save the product definition, including problem, persona, promise, MVP, non-goals, North Star Metric, and success targets.

### 2 · 5-Gate Review
Each gate has its own score and evidence:

1. Customer Value
2. AI Quality
3. Trust & Safety
4. Operational Readiness
5. Business Readiness

### 3 · Risk & Trust
Every risk has independent state for title, category, likelihood, impact, mitigation, and owner. Risks can be added, edited, deleted, and reset to demo data. Exposure is calculated as:

`Likelihood × Impact`

### 4 · AI Evaluation
Evaluation cases can be edited independently. Aggregate quality, safety, and pass-rate metrics are recalculated from the saved cases.

### 5 · Executive Decision
The decision page is a synthesis layer. It consumes the saved gate review, risk register, and AI evaluation state and returns **GO**, **ITERATE**, or **NO-GO**.

## Architecture

```text
                    ┌─────────────────────┐
                    │   Product Brief     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   5 Launch Gates    │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┴─────────────────┐
             ▼                                   ▼
   ┌─────────────────────┐             ┌─────────────────────┐
   │ Risk & Trust        │             │ AI Evaluation       │
   │ independent records │             │ independent cases   │
   └──────────┬──────────┘             └──────────┬──────────┘
              └────────────────┬──────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Decision Engine     │
                    │ GO / ITERATE / NO-GO│
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Executive Memo      │
                    └─────────────────────┘
```

## State-management design

Streamlit reruns the script after widget interaction. LaunchPilot therefore stores editable workspace data in `st.session_state` and gives each interactive object a unique namespace/key. The Risk Register intentionally avoids a single shared editor state for multiple risk rows; each risk is edited in its own form using a stable risk ID.

This prevents the bug where changing one row's Likelihood/Impact unexpectedly changes other rows.

## Local setup — Windows + Anaconda

```bash
conda create -n launchpilot python=3.12 -y
conda activate launchpilot
cd C:\path\to\launchpilot-ai
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
pytest -q
python -m compileall app.py core tests
streamlit run app.py
```

Open `http://localhost:8501`.

## QA checklist

Before deployment, manually verify:

- [ ] Edit Product Brief and save; other sections remain unchanged.
- [ ] Change only Customer Value; other gates remain unchanged.
- [ ] Change only Hallucinated policy answer; all other risks remain unchanged.
- [ ] Add and delete a risk.
- [ ] Change one AI evaluation case; other cases remain unchanged.
- [ ] Verify Executive Decision updates from saved inputs.
- [ ] Download AI PRD, evaluation CSV, and executive memo.
- [ ] Refresh the app and verify the current session remains coherent.

## Tests

The repository includes regression tests for independent state at the domain/data layer:

```bash
pytest -q
```

## Deployment

The repository is structured for Streamlit Community Cloud:

- `app.py` is the root entrypoint.
- `requirements.txt` is in the repository root.
- `.streamlit/config.toml` is included.
- All local paths use `pathlib` rather than Windows-only paths.

Create a Streamlit Community Cloud app from your GitHub repository and select:

- Repository: `YOUR_USERNAME/launchpilot-ai`
- Branch: `main`
- Main file: `app.py`
- Python: 3.12

## 📸 Product Demo

LaunchPilot AI is an interactive product-management decision system that takes a product from initial definition through AI evaluation, launch readiness, risk assessment, and executive decision-making.

### 1. Product Brief

Define the product, target customer, problem, product promise, MVP scope, and success metrics.

![LaunchPilot AI — Product Brief](screenshots/01-product-brief.png)

---

### 2. 5-Gate Launch Review

Evaluate the product across five launch-readiness dimensions:

- Customer Value
- AI Quality
- Trust & Safety
- Operational Readiness
- Business Readiness

![LaunchPilot AI — 5-Gate Review](screenshots/02-five-gate-review.png)

---

### 3. Risk & Trust

Identify, score, prioritize, and mitigate product and AI risks using likelihood × impact exposure.

![LaunchPilot AI — Risk & Trust](screenshots/03-risk-trust.png)

---

### 4. AI Evaluation

Evaluate AI product quality, safety, and test-case performance before launch.

![LaunchPilot AI — AI Evaluation](screenshots/04-ai-evaluation.png)

---

### 5. Executive Decision

Synthesize product, launch-gate, risk, and AI evaluation evidence into an executive GO / ITERATE / NO-GO decision.

![LaunchPilot AI — Executive Decision](screenshots/05-executive-decision.png)

## Project positioning for PM interviews

LaunchPilot demonstrates a complete launch-management loop:

**Problem framing → MVP → evaluation → risk management → launch gates → decision → executive communication.**

Do not describe synthetic demo values as real business results.

## Author

**Abhishek Kumar Gond**  
IIT Guwahati 
- **Email : mr.abhishekaaa@gmail.com**
- **[Portfolio]()**
- **[LinkedIn](https://www.linkedin.com/in/abhishekkumargond/)**

## License

Released under the [MIT License](LICENSE).

