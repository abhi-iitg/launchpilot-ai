from core.decision_engine import Gate, Risk, decision, overall_score, risk_level


def test_gate_passes_threshold():
    assert Gate("Customer Value", 70).passed
    assert not Gate("Customer Value", 69).passed


def test_risk_levels():
    assert risk_level(16) == "Critical"
    assert risk_level(9) == "High"
    assert risk_level(4) == "Medium"
    assert risk_level(1) == "Low"


def test_no_go_on_critical_gate():
    gates = [Gate("Customer Value", 80), Gate("AI Quality", 65, critical=True)]
    result = decision(gates, [])
    assert result["verdict"] == "NO-GO"


def test_iterate_on_failed_noncritical_gate():
    gates = [Gate("Customer Value", 80), Gate("Business Readiness", 65)]
    result = decision(gates, [])
    assert result["verdict"] == "ITERATE"


def test_go_when_all_clear():
    gates = [Gate("Customer Value", 80), Gate("AI Quality", 85, critical=True), Gate("Trust & Safety", 90, critical=True)]
    result = decision(gates, [])
    assert result["verdict"] == "GO"


def test_critical_risk_forces_no_go():
    gates = [Gate("Customer Value", 90), Gate("AI Quality", 90, critical=True)]
    risks = [Risk("Data leak", "Privacy", 4, 4, "Fix", "Security")]
    result = decision(gates, risks)
    assert result["verdict"] == "NO-GO"
    assert "Data leak" in result["critical_risks"]


def test_overall_score():
    assert overall_score([Gate("A", 80), Gate("B", 90)]) == 85.0


def test_critical_evaluation_blocker_forces_no_go():
    gates = [Gate("Customer Value", 90), Gate("AI Quality", 90, critical=True)]
    result = decision(gates, [], critical_blockers=["AI Evaluation threshold not met"])
    assert result["verdict"] == "NO-GO"
    assert "AI Evaluation threshold not met" in result["critical_blockers"]
