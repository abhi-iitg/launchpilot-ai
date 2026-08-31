from copy import deepcopy

from core.decision_engine import Risk, risk_level, risk_rows
from core.risk_register import clean_risk_records, clone_seed_risks, risk_objects


def test_seed_risks_are_independent_records():
    risks = clone_seed_risks()
    risks[0]["likelihood"] = 4
    assert risks[0]["likelihood"] == 4
    assert risks[1]["likelihood"] == 2
    assert clone_seed_risks()[0]["likelihood"] == 2


def test_editing_one_seed_risk_does_not_change_other_risks():
    risks = clone_seed_risks()
    risks[0]["likelihood"] = 4
    risks[0]["impact"] = 2
    cleaned = clean_risk_records(risks)

    assert cleaned[0]["likelihood"] == 4
    assert cleaned[0]["impact"] == 2
    assert cleaned[1]["likelihood"] == 2
    assert cleaned[1]["impact"] == 5
    assert cleaned[2]["likelihood"] == 3
    assert cleaned[2]["impact"] == 4


def test_new_rows_are_sanitized_and_clamped():
    cleaned = clean_risk_records([
        {
            "title": "New risk",
            "category": "Operations",
            "likelihood": 99,
            "impact": 0,
            "mitigation": "Test mitigation",
            "owner": "PM",
        },
        {"title": "   "},
    ])
    assert len(cleaned) == 1
    assert cleaned[0]["likelihood"] == 5
    assert cleaned[0]["impact"] == 1


def test_risk_objects_preserve_row_values():
    records = clean_risk_records(clone_seed_risks())
    risks = risk_objects(records)
    assert risks[0].exposure == 10
    assert risks[1].exposure == 10
    assert risks[2].exposure == 12


def test_risk_exposure_is_row_specific():
    first = Risk("A", "AI", 2, 5, "Fix A", "PM")
    second = Risk("B", "Privacy", 3, 4, "Fix B", "Security")
    assert first.exposure == 10
    assert second.exposure == 12


def test_risk_rows_keep_each_risk_independent():
    rows = risk_rows(
        [
            Risk("A", "AI", 2, 5, "Fix A", "PM"),
            Risk("B", "Privacy", 3, 4, "Fix B", "Security"),
        ]
    )
    assert rows[0]["likelihood"] == 2
    assert rows[0]["impact"] == 5
    assert rows[0]["Exposure"] == 10
    assert rows[1]["likelihood"] == 3
    assert rows[1]["impact"] == 4
    assert rows[1]["Exposure"] == 12


def test_exposure_level_boundaries():
    assert risk_level(3) == "Low"
    assert risk_level(4) == "Medium"
    assert risk_level(8) == "Medium"
    assert risk_level(9) == "High"
    assert risk_level(15) == "High"
    assert risk_level(16) == "Critical"
