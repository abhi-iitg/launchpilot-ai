# AI PRD — ResolveAI

## 1. Product goal
Help SaaS customers resolve routine support questions quickly while preserving trust through source grounding and human escalation.

## 2. User problem
Customers often wait for answers to repetitive questions. Support agents spend time on low-complexity tickets instead of high-value cases.

## 3. Users
- Primary: SaaS customers asking product/policy questions
- Secondary: Support agents who receive escalations
- Buyer: Head of Customer Support / VP Customer Experience

## 4. Jobs to be done
> When I have a product or policy question, help me get a correct answer quickly; when the system is uncertain, make the handoff to a human obvious and low-friction.

## 5. MVP
1. Source-cited answer generation
2. Confidence-gated escalation
3. Agent handoff
4. Feedback capture
5. Evaluation dashboard
6. Launch scorecard

## 6. Non-goals
- Autonomous account changes
- Refunds or credits
- Legal/financial advice
- Unbounded actions
- Replacing human support for complex cases

## 7. Functional requirements
- Every factual answer must be traceable to an approved source.
- The system must provide an explicit escalation path.
- High-risk requests must not be answered beyond approved scope.
- Feedback must be captured for answer quality review.
- Product metrics must distinguish self-resolution from successful human handoff.

## 8. AI requirements
- Evaluate groundedness and task success before launch.
- Test adversarial and privacy-sensitive prompts.
- Track severe hallucinations separately from low-severity quality errors.
- Use confidence thresholds as a product policy, not merely a model setting.

## 9. Acceptance criteria
A controlled rollout is eligible when all critical gates pass and no critical risk remains open.
