from dataclasses import dataclass, asdict
from typing import List, Dict

GATES = [
    "Customer Value",
    "AI Quality",
    "Trust & Safety",
    "Operational Readiness",
    "Business Readiness",
]

@dataclass
class Gate:
    name: str
    score: int
    threshold: int = 70
    critical: bool = False
    evidence: str = ""

    @property
    def passed(self) -> bool:
        return self.score >= self.threshold

@dataclass
class Risk:
    title: str
    category: str
    likelihood: int
    impact: int
    mitigation: str
    owner: str

    @property
    def exposure(self) -> int:
        return self.likelihood * self.impact


def risk_level(exposure: int) -> str:
    if exposure >= 16:
        return "Critical"
    if exposure >= 9:
        return "High"
    if exposure >= 4:
        return "Medium"
    return "Low"


def overall_score(gates: List[Gate]) -> float:
    return round(sum(g.score for g in gates) / len(gates), 1) if gates else 0.0


def decision(gates: List[Gate], risks: List[Risk], business_target_met: bool = True, critical_blockers: List[str] | None = None) -> Dict:
    critical_failures = [g.name for g in gates if g.critical and not g.passed]
    critical_blockers = list(critical_blockers or [])
    failed = [g.name for g in gates if not g.passed]
    critical_risks = [r.title for r in risks if r.exposure >= 16]
    high_risks = [r.title for r in risks if 9 <= r.exposure < 16]
    score = overall_score(gates)

    if critical_failures or critical_risks or critical_blockers:
        verdict = "NO-GO"
        rationale = "A critical launch gate or critical risk remains unresolved."
    elif failed or high_risks or not business_target_met:
        verdict = "ITERATE"
        rationale = "The product shows promise, but launch evidence or risk controls are not yet strong enough for a broad release."
    else:
        verdict = "GO"
        rationale = "All launch gates clear their thresholds and no high-severity blocker remains."

    return {
        "verdict": verdict,
        "overall_score": score,
        "failed_gates": failed,
        "critical_failures": critical_failures,
        "critical_risks": critical_risks,
        "critical_blockers": critical_blockers,
        "high_risks": high_risks,
        "rationale": rationale,
        "gate_pass_rate": round(100 * sum(g.passed for g in gates) / len(gates), 1) if gates else 0.0,
    }


def scorecard_rows(gates: List[Gate]) -> List[Dict]:
    return [
        {
            "Gate": g.name,
            "Score": g.score,
            "Threshold": g.threshold,
            "Status": "PASS" if g.passed else "FAIL",
            "Critical": "Yes" if g.critical else "No",
            "Evidence": g.evidence,
        }
        for g in gates
    ]


def risk_rows(risks: List[Risk]) -> List[Dict]:
    return [
        {
            **asdict(r),
            "Exposure": r.exposure,
            "Level": risk_level(r.exposure),
        }
        for r in risks
    ]
