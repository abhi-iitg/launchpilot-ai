# Changelog

## 1.2.0 — State & Interaction Reliability Release

- Rebuilt the five workspace sections around explicit session-state namespaces.
- Product Brief now has an independent save workflow.
- Each launch gate has independent score/evidence state.
- Risk Register now uses stable IDs and one independent form per risk.
- Added add/edit/delete/reset risk workflows.
- AI Evaluation cases are independently editable and aggregate metrics are recalculated.
- Executive Decision now synthesizes saved workspace state and treats failed AI evaluation thresholds as critical blockers.
- Added regression tests for cross-record independence and launch blocking.
- Added Windows one-click runner and deployment/QA documentation.
