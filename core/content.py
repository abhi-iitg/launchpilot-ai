from typing import Dict, List


def build_prd(product: Dict) -> str:
    return f"""# {product['name']} — AI Product Requirements Brief\n\n## Problem\n{product['problem']}\n\n## Target user\n{product['persona']}\n\n## Product promise\n{product['promise']}\n\n## MVP\n{product['mvp']}\n\n## Non-goals\n{product['non_goals']}\n\n## North Star Metric\n{product['north_star']}\n\n## Success targets\n{product['success_targets']}\n\n## AI quality requirement\nThe AI must be evaluated on groundedness, task success, refusal behavior, and escalation quality before broad release.\n"""


def build_decision_memo(product: Dict, result: Dict, next_steps: List[str]) -> str:
    bullets = "\n".join(f"- {x}" for x in next_steps)
    failed = ", ".join(result["failed_gates"]) or "None"
    critical = ", ".join(result["critical_risks"]) or "None"
    return f"""# Executive Launch Decision Memo\n\n**Product:** {product['name']}  \n**Decision:** **{result['verdict']}**  \n**Overall readiness:** {result['overall_score']}/100  \n**Gate pass rate:** {result['gate_pass_rate']}%\n\n## Executive rationale\n{result['rationale']}\n\n## Failed gates\n{failed}\n\n## Critical risks\n{critical}\n\n## Recommended next actions\n{bullets}\n\n## PM principle\nLaunch decisions should be evidence-led: customer value, AI quality, trust, operations, and business value must be considered together rather than optimizing one dimension in isolation.\n"""
