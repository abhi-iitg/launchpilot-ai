"""Risk register seed data, validation, and domain conversion."""
from __future__ import annotations

from copy import deepcopy
from uuid import uuid4

from core.decision_engine import Risk

SEED_RISKS = [
    {"id": "risk-1", "title": "Hallucinated policy answer", "category": "AI Quality", "likelihood": 2, "impact": 5, "mitigation": "Require source grounding, confidence threshold, and human escalation.", "owner": "AI PM"},
    {"id": "risk-2", "title": "Sensitive customer data exposure", "category": "Privacy", "likelihood": 2, "impact": 5, "mitigation": "Minimize data, redact sensitive fields, deny cross-account requests, log access.", "owner": "Security"},
    {"id": "risk-3", "title": "Silent AI failure after launch", "category": "Operations", "likelihood": 3, "impact": 4, "mitigation": "Monitor quality, latency, escalation rate and set rollback thresholds.", "owner": "Engineering"},
    {"id": "risk-4", "title": "Low customer adoption", "category": "Business", "likelihood": 3, "impact": 3, "mitigation": "Instrument onboarding and test value messaging before broad rollout.", "owner": "Growth PM"},
    {"id": "risk-5", "title": "Agent handoff overload", "category": "Operations", "likelihood": 3, "impact": 4, "mitigation": "Tune confidence threshold and add routing/queue capacity guardrails.", "owner": "Support Ops"},
]


def clone_seed_risks() -> list[dict]:
    return deepcopy(SEED_RISKS)


def clean_risk_records(records: list[dict]) -> list[dict]:
    cleaned = []
    for row in records:
        title = str(row.get("title", "") or "").strip()
        if not title:
            continue
        category = str(row.get("category", "Business") or "Business").strip() or "Business"
        mitigation = str(row.get("mitigation", "") or "").strip()
        owner = str(row.get("owner", "Product") or "Product").strip() or "Product"
        try:
            likelihood = int(row.get("likelihood", 1))
        except (TypeError, ValueError):
            likelihood = 1
        try:
            impact = int(row.get("impact", 1))
        except (TypeError, ValueError):
            impact = 1
        cleaned.append({
            "id": str(row.get("id") or uuid4()),
            "title": title,
            "category": category,
            "likelihood": max(1, min(5, likelihood)),
            "impact": max(1, min(5, impact)),
            "mitigation": mitigation,
            "owner": owner,
        })
    return cleaned


def risk_objects(records: list[dict]) -> list[Risk]:
    return [Risk(title=r["title"], category=r["category"], likelihood=r["likelihood"], impact=r["impact"], mitigation=r["mitigation"], owner=r["owner"]) for r in clean_risk_records(records)]
