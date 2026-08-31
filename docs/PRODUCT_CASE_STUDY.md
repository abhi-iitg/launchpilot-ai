# Product Case Study — ResolveAI

## Executive summary
ResolveAI is a fictional AI customer-support product designed around a simple product thesis: **AI should resolve routine support work quickly, but uncertainty must be visible and recoverable.**

The project demonstrates how a PM can turn an AI capability into a launchable product by connecting customer value, evaluation, trust, operations and business readiness.

## Problem framing
Support teams face repetitive questions, while customers value speed and clarity. A generic chatbot can reduce cost but can also introduce trust-damaging errors. The product therefore focuses on bounded, source-grounded support intents.

## Product strategy
The strategy is not “automate support.” It is:

> **Automate low-risk, high-frequency questions while preserving a high-quality human escape hatch.**

## Key product decisions

### Decision 1 — Bounded scope
Autonomous account changes and sensitive actions are excluded from MVP. This reduces downside risk while allowing the product to prove value on well-documented intents.

### Decision 2 — Confidence-gated escalation
The system should not optimize only for answer rate. When confidence or evidence is insufficient, escalation becomes a successful product outcome rather than a failure.

### Decision 3 — Quality as a launch gate
Aggregate AI quality is insufficient. Severe hallucination and unsafe behavior can block launch even when average quality looks strong.

### Decision 4 — Controlled rollout
The first launch is intentionally small. Real customer behavior is needed to validate adoption, operational capacity and trust.

## Prioritization

| Feature | Customer value | Risk reduction | Effort | Priority |
|---|---|---|---|---|
| Source-cited answers | High | High | Medium | P0 |
| Confidence escalation | High | High | Medium | P0 |
| Agent handoff | High | High | Medium | P0 |
| Feedback capture | Medium | Medium | Low | P0 |
| Evaluation dashboard | High | High | Medium | P0 |
| Autonomous refunds | Medium | Low | High | P2 / excluded |

## Experiment backlog

1. Does source citation increase trust and self-resolution?
2. What confidence threshold minimizes both wrong answers and unnecessary escalation?
3. Does a guided handoff reduce customer frustration after escalation?
4. Which intent categories produce the highest safe automation rate?

## Interview takeaway

The project is intentionally designed to show **PM judgment**, not just implementation. The strongest decisions are scope boundaries, launch gates, rollout design, metrics and trade-offs.
