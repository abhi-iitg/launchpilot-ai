# Product Metrics Tree

## North Star Metric

**Resolved Customer Sessions (RCS)**

A session counts when the customer receives a correct answer or completes a successful human handoff without reopening the same issue.

```text
Resolved Customer Sessions
├── Self-resolution rate
│   ├── Answer correctness
│   ├── Groundedness
│   └── Completion rate
├── Human-handoff success
│   ├── Escalation precision
│   └── Agent acceptance rate
└── Trust / quality
    ├── Severe hallucination rate
    ├── CSAT
    └── Privacy incidents
```

## Guardrails

- Severe hallucination <5%
- Privacy incidents = 0
- Escalation overload below support capacity
- p95 latency within agreed SLA

## Product decision loop

**Measure → diagnose → prioritize → experiment → re-measure.**
