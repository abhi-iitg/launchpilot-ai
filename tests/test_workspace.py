from core.workspace import DEMO_BRIEF, brief_to_dict, clone_seed_evals, evaluation_summary, sanitize_brief, sanitize_evals


def test_product_brief_fields_are_independent():
    brief = brief_to_dict(DEMO_BRIEF)
    brief["name"] = "Changed Product"
    assert brief["name"] == "Changed Product"
    assert brief["problem"] == DEMO_BRIEF.problem
    assert brief["north_star"] == DEMO_BRIEF.north_star


def test_brief_sanitizer_preserves_unedited_values():
    cleaned = sanitize_brief({"name": "My Product"})
    assert cleaned["name"] == "My Product"
    assert cleaned["category"] == DEMO_BRIEF.category
    assert cleaned["mvp"] == DEMO_BRIEF.mvp


def test_evaluation_cases_are_independent():
    cases = clone_seed_evals()
    cases[0]["quality"] = 10
    assert cases[0]["quality"] == 10
    assert cases[1]["quality"] == 90


def test_evaluation_values_are_clamped():
    cleaned = sanitize_evals([{"id": "x", "case": "A", "expected": "B", "quality": 999, "safety": -4}])
    assert cleaned[0]["quality"] == 100
    assert cleaned[0]["safety"] == 0


def test_evaluation_summary_is_live():
    cases = clone_seed_evals()
    summary = evaluation_summary(cases)
    assert summary["quality"] > 80
    assert summary["safety"] > 90
    assert summary["status"] == "PASS"

    cases[0]["safety"] = 10
    summary2 = evaluation_summary(cases)
    assert summary2["safety"] < summary["safety"]


def test_one_evaluation_edit_does_not_change_other_cases():
    cases = clone_seed_evals()
    cases[2]["quality"] = 20
    cases[2]["safety"] = 30
    assert cases[2]["quality"] == 20
    assert cases[2]["safety"] == 30
    assert cases[0]["quality"] == 95
    assert cases[0]["safety"] == 98
    assert cases[3]["quality"] == 92


def test_saved_risk_records_keep_stable_ids():
    from core.risk_register import clean_risk_records, clone_seed_risks
    records = clean_risk_records(clone_seed_risks())
    assert [r["id"] for r in records] == ["risk-1", "risk-2", "risk-3", "risk-4", "risk-5"]


def test_gate_score_vector_changes_only_selected_gate():
    scores = [82, 88, 91, 78, 76]
    updated = list(scores)
    updated[2] = 55
    assert updated[2] == 55
    assert updated[0] == 82
    assert updated[1] == 88
    assert updated[3] == 78
    assert updated[4] == 76
