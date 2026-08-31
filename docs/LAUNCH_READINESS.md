# Launch Readiness Framework

## Gate 1 — Customer Value
**Question:** Are we solving a meaningful problem?

Evidence:
- Clear persona
- Defined JTBD
- MVP scope tied to the problem
- North Star metric
- Success targets

## Gate 2 — AI Quality
**Question:** Is the AI good enough for the intended task?

Evidence:
- Evaluation dataset
- Groundedness score
- Task success
- Refusal quality
- Escalation precision

## Gate 3 — Trust & Safety
**Question:** Can customers trust the system?

Evidence:
- Risk register
- Privacy controls
- Out-of-scope behavior
- Prompt-injection tests
- High-severity failure policy

## Gate 4 — Operational Readiness
**Question:** Can the team monitor and recover from failures?

Evidence:
- Monitoring metrics
- Human escalation
- Rollback plan
- Support ownership
- Incident response

## Gate 5 — Business Readiness
**Question:** Is there a measurable business case?

Evidence:
- Ticket deflection target
- CSAT target
- Cost-to-serve hypothesis
- Adoption plan
- Controlled rollout

## Decision rules

- **GO:** all critical gates pass; no critical risk remains.
- **ITERATE:** no critical blocker, but one or more non-critical gaps remain.
- **NO-GO:** any critical gate fails or a critical risk remains open.
