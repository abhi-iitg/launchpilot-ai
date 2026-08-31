# 🚀 LaunchPilot AI

**AI Product Launch & Decision OS for evidence-led product discovery, AI evaluation, trust & safety, launch readiness, and executive decision-making.**

> **Portfolio project for Product Management.** Demo data and outcomes are synthetic and illustrative.

## 🚀 Live Demo

[LaunchPilot AI — Live Demo](https://launchpilot-ai-abhi-iitg.streamlit.app/)

---

## 📑 Table of Contents

-   [🎯 Product Overview](#-product-overview)
-   [🔍 Problem](#-problem)
-   [🔄 Live Product Workflow](#-live-product-workflow)
-   [🧠 PM Capabilities Demonstrated](#-pm-capabilities-demonstrated)
-   [🚀 Key Product Features](#-key-product-features)
    -   [1 · Product Brief](#1--product-brief)
    -   [2 · 5-Gate Review](#2--5-gate-review)
    -   [3 · Risk & Trust](#3--risk--trust)
    -   [4 · AI Evaluation](#4--ai-evaluation)
    -   [5 · Executive Decision](#5--executive-decision)
-   [🏗️ Architecture](#️-architecture)
-   [⚙️ State-Management Design](#️-state-management-design)
-   [💻 Local Setup --- Windows +
    Anaconda](#-local-setup--windows--anaconda)
-   [✅ QA Checklist](#-qa-checklist)
-   [🧪 Tests](#-tests)
-   [☁️ Deployment](#️-deployment)
-   [📸 Product Demo](#-product-demo)
-   [🎯 Project Positioning for PM
    Interviews](#-project-positioning-for-pm-interviews)
-   [👤 Author](#-author)
-   [📄 License](#-license)

---

## 🎯 Product Overview

**LaunchPilot AI** is an AI Product Launch & Decision OS designed to help product managers move from **product definition to evidence-based launch decisions**.

The platform brings together the core activities required to evaluate an AI-enabled product before launch:

-   **Product Brief** --- define the target customer, problem, product promise, MVP scope, and success           metrics.
-   **5-Gate Launch Review** --- assess Customer Value, AI Quality, Trust & Safety, Operational Readiness,      and Business Readiness.
-   **Risk & Trust Management** --- identify, score, prioritize, and mitigate product and AI risks using        likelihood × impact exposure.
-   **AI Evaluation** --- evaluate AI behavior across structured test cases using quality and safety            criteria.
-   **Executive Decision** --- synthesize product, launch-gate, risk, and AI-evaluation evidence into a         clear **GO / ITERATE / NO-GO** recommendation.

### Product Objective

The objective is to reduce the gap between **building an AI feature** and deciding whether that feature is actually **ready to launch**.

Instead of treating launch readiness as a subjective discussion, LaunchPilot AI creates a structured decision workflow:

``` text
Product Definition
        ↓
Customer & Business Value
        ↓
AI Quality Evaluation
        ↓
Trust & Safety Assessment
        ↓
Operational Readiness
        ↓
Risk Assessment
        ↓
Launch Readiness
        ↓
Executive Decision
        ↓
GO / ITERATE / NO-GO
```

### Who Is It For?

**Primary users**

-   Product Managers
-   AI Product Managers
-   Product Leads
-   Startup Founders
-   Product Operations teams
-   AI governance and risk stakeholders

**Typical use case**

A product team is preparing to launch an AI-powered capability. Before launch, the team needs to answer:

> **Is the product valuable, safe, reliable, operationally ready, and
> commercially ready enough to launch?**

LaunchPilot AI provides a structured framework for answering that question using measurable evidence rather than intuition alone.

### Product Philosophy

> **A product should not launch because it was built. It should launch
> because the evidence supports launching it.**

The platform therefore connects **product strategy, AI evaluation, risk management, and executive decision-making** into one workflow.

---

## 🔍 Problem

AI products introduce a unique product-management challenge: **building the feature is only the beginning**.

A team may have a technically functional AI capability but still lack confidence about whether it delivers meaningful customer value, produces reliable outputs, handles risky situations safely, or is operationally
ready for real users.

Traditional product launch processes can also become fragmented across multiple documents, spreadsheets, dashboards, and stakeholder discussions.

### The Core Problem

Product teams often need to answer several questions before launching an
AI-powered feature:

  -----------------------------------------------------------------------
  Product Question                    What Can Go Wrong?
  ----------------------------------- -----------------------------------
  **Does it solve a real customer     The feature may have low customer
  problem?**                          value or weak product-market
                                      relevance.

  **Does the AI perform reliably?**   Hallucinations, inconsistent
                                      outputs, or poor task performance
                                      may reduce trust.

  **Is it safe and trustworthy?**     The system may generate harmful,
                                      misleading, privacy-sensitive, or
                                      policy-inconsistent responses.

  **Are operational teams ready?**    Support, monitoring, escalation,
                                      and incident processes may not be
                                      prepared.

  **Is the business ready?**          Costs, adoption assumptions, GTM
                                      plans, and success metrics may be
                                      unclear.

  **What are the highest launch       Critical risks may be identified
  risks?**                            but not quantified or connected to
                                      the launch decision.

  **Should the product launch now?**  Stakeholders may disagree because
                                      evidence is fragmented across
                                      different sources.
  -----------------------------------------------------------------------

### Why This Matters More for AI Products

AI systems can behave differently across inputs and can introduce additional uncertainty around:

-   Output quality
-   Hallucination
-   Safety
-   Reliability
-   Bias
-   Privacy
-   Policy compliance
-   Human escalation
-   Monitoring
-   Model degradation

This creates a product-management requirement beyond the traditional:

``` text
Build → Test → Launch
```

AI products require a broader workflow:

``` text
Define
  ↓
Validate Customer Value
  ↓
Evaluate AI
  ↓
Assess Trust & Safety
  ↓
Assess Operational Readiness
  ↓
Quantify Risks
  ↓
Review Business Readiness
  ↓
Make Launch Decision
```

### The Product Gap

Without a structured system, launch evidence can become fragmented:

``` text
PRD
 ├── Product requirements

Risk Register
 ├── Product and AI risks

AI Evaluation
 ├── Model test results

Operations
 ├── Readiness checklist

Business Team
 ├── GTM assumptions

Leadership
 └── Final launch discussion
```

The result is a decision-making gap:

> **The evidence exists, but it is not always connected to the final
> launch decision.**

### LaunchPilot AI's Solution

LaunchPilot AI connects these components into a single decision workflow:

``` text
                    ┌──────────────────┐
                    │  Product Brief   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │   5 Launch Gates │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Risk & Trust     │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ AI Evaluation    │
                    └────────┬─────────┘
                             ↓
                 ┌────────────────────────┐
                 │ Executive Decision     │
                 │ GO / ITERATE / NO-GO   │
                 └────────────────────────┘
```

### Success Definition

LaunchPilot AI succeeds when a product team can move from fragmented product, AI, risk, and business evidence to a **clear, explainable, and defensible launch decision**.

> **From Product Idea → Evidence → Launch Readiness → Executive
> Decision.**

---

## 🔄 Live Product Workflow

``` text
Product Brief
      ↓
5-Gate Review
      ↓
Risk & Trust
      ↓
AI Evaluation
      ↓
Executive Decision
      ↓
GO / ITERATE / NO-GO
```
---

## 🧠 PM Capabilities Demonstrated

  -----------------------------------------------------------------------
  PM Capability                       Demonstrated Through
  ----------------------------------- -----------------------------------
  Product Discovery                   Problem definition, target user,
                                      product promise

  PRD Development                     Product Brief and MVP scope

  Product Strategy                    Product goals, North Star Metric
                                      and success criteria

  AI Product Management               AI evaluation and quality
                                      thresholds

  Responsible AI                      Trust & Safety assessment

  Risk Management                     Likelihood × Impact risk framework

  Product Analytics                   Readiness metrics and evaluation
                                      metrics

  Experimentation                     AI evaluation cases and launch
                                      criteria

  Go-to-Market                        Launch and rollout planning

  Executive Communication             Executive Decision Memo

  Decision Making                     GO / ITERATE / NO-GO framework
  -----------------------------------------------------------------------
---

## 🚀 Key Product Features

### 1 · Product Brief
Edit and save the product definition, including problem, persona, promise, MVP, non-goals, North Star Metric, and success targets.

### 2 · 5-Gate Review
Each gate has its own score and evidence:

1. Customer Value
2. AI Quality
3. Trust & Safety
4. Operational Readiness
5. Business Readiness

### 3 · Risk & Trust
Every risk has independent state for title, category, likelihood, impact, mitigation, and owner. Risks can be added, edited, deleted, and reset to demo data. Exposure is calculated as:

`Likelihood × Impact`

### 4 · AI Evaluation
Evaluation cases can be edited independently. Aggregate quality, safety, and pass-rate metrics are recalculated from the saved cases.

### 5 · Executive Decision
The decision page is a synthesis layer. It consumes the saved gate review, risk register, and AI evaluation state and returns **GO**, **ITERATE**, or **NO-GO**.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   Product Brief     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   5 Launch Gates    │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┴─────────────────┐
             ▼                                   ▼
   ┌─────────────────────┐             ┌─────────────────────┐
   │ Risk & Trust        │             │ AI Evaluation       │
   │ independent records │             │ independent cases   │
   └──────────┬──────────┘             └──────────┬──────────┘
              └────────────────┬──────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Decision Engine     │
                    │ GO / ITERATE / NO-GO│
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Executive Memo      │
                    └─────────────────────┘
```
---

## ⚙️ State-Management Design

Streamlit reruns the script after widget interaction. LaunchPilot therefore stores editable workspace data in `st.session_state` and gives each interactive object a unique namespace/key.

The Risk Register intentionally avoids a single shared editor state for multiple risk rows. Each risk is edited independently using a stable risk ID.

This prevents the bug where changing one row's Likelihood/Impact unexpectedly changes other rows.

The same principle is applied across:

-   Product Brief fields
-   Five launch gates
-   Risk records
-   AI evaluation cases

The Executive Decision page reads the saved state rather than maintaining a second, conflicting copy of the decision inputs.

---

## 💻 Local Setup --- Windows + Anaconda

### 1. Create the environment

``` bash
conda create -n launchpilot python=3.12 -y
```

### 2. Activate the environment

``` bash
conda activate launchpilot
```

### 3. Move to the project directory

``` bash
cd C:\path\to\launchpilot-ai
```

### 4. Upgrade pip

``` bash
python -m pip install --upgrade pip
```

### 5. Install application dependencies

``` bash
pip install -r requirements.txt
```

### 6. Install development/testing dependencies

``` bash
pip install -r requirements-dev.txt
```

### 7. Run tests

``` bash
pytest -q
```

### 8. Compile-check the project

``` bash
python -m compileall app.py core tests
```

### 9. Start the application

``` bash
streamlit run app.py
```

Open:

``` text
http://localhost:8501
```

---

## ✅ QA Checklist

Before deployment, manually verify:

-   [ ] Edit Product Brief and save; other sections remain unchanged.
-   [ ] Change only one 5-Gate score; other gates remain unchanged.
-   [ ] Change only the Hallucinated Policy Answer risk; all other risks
    remain unchanged.
-   [ ] Add and delete a risk.
-   [ ] Change one AI evaluation case; other cases remain unchanged.
-   [ ] Verify risk exposure recalculates correctly from Likelihood ×
    Impact.
-   [ ] Verify Executive Decision updates from saved inputs.
-   [ ] Verify Executive Decision contains Product Brief, Gate Review,
    Risk & Trust, AI Evaluation, and Decision Summary tables.
-   [ ] Download AI PRD, evaluation CSV, and executive memo.
-   [ ] Refresh the app and verify the current session remains coherent.
-   [ ] Verify the deployed application opens successfully.
-   [ ] Verify the deployed application works independently of the local
    development environment.

---

## 🧪 Tests

The repository includes regression tests for the decision engine, risk calculations, evaluation logic, and independent state at the domain/data layer.

Run:

``` bash
pytest -q
```

Compile-check:

``` bash
python -m compileall app.py core tests
```

The README intentionally does not hard-code temporary test counts or demo scores. Run the commands above against the current repository version for the authoritative result.

---

## ☁️ Deployment

The repository is structured for Streamlit Community Cloud:

- `app.py` is the root entrypoint.
- `requirements.txt` is in the repository root.
- `.streamlit/config.toml` is included.
- All local paths use `pathlib` rather than Windows-only paths.

### Streamlit Community Cloud

Create a Streamlit Community Cloud app from the GitHub repository and
select:

-   **Repository:** `YOUR_USERNAME/launchpilot-ai`
-   **Branch:** `main`
-   **Main file:** `app.py`
-   **Python:** `3.12`

### Deployment checklist

``` text
GitHub Repository
      ↓
requirements.txt
      ↓
app.py
      ↓
Streamlit Community Cloud
      ↓
Public Live Demo
```
After deployment, test all five product sections before adding the live
URL to your resume.

---

## 📸 Product Demo

Store screenshots in:

``` text
screenshots/
├── 01-product-brief.png
├── 02-five-gate-review.png
├── 03-risk-trust.png
├── 04-ai-evaluation.png
└── 05-executive-decision.png
```

### 1. Product Brief

Define the product, target customer, problem, product promise, MVP scope, and success metrics.

![LaunchPilot AI — Product Brief](screenshots/01-product-brief.png)

---

### 2. 5-Gate Launch Review

Evaluate the product across five launch-readiness dimensions:

- Customer Value
- AI Quality
- Trust & Safety
- Operational Readiness
- Business Readiness

![LaunchPilot AI — 5-Gate Review](screenshots/02-five-gate-review.png)

---

### 3. Risk & Trust

Identify, score, prioritize, and mitigate product and AI risks using likelihood × impact exposure.

![LaunchPilot AI — Risk & Trust](screenshots/03-risk-trust.png)

---

### 4. AI Evaluation

Evaluate AI product quality, safety, and test-case performance before launch.

![LaunchPilot AI — AI Evaluation](screenshots/04-ai-evaluation.png)

---

### 5. Executive Decision

Synthesize product, launch-gate, risk, and AI evaluation evidence into an executive GO / ITERATE / NO-GO decision.

![LaunchPilot AI — Executive Decision](screenshots/05-executive-decision.png)

## 🎯 Project Positioning for PM Interviews

LaunchPilot AI demonstrates a complete product launch-management loop:

``` text
Problem Framing
      ↓
Product Definition
      ↓
MVP & Success Metrics
      ↓
AI Evaluation
      ↓
Risk & Trust Management
      ↓
Launch Gates
      ↓
Executive Decision
      ↓
GO / ITERATE / NO-GO
      ↓
Executive Communication
```

### What This Project Demonstrates

The project is designed to demonstrate practical Product Management skills rather than only software implementation:

-   Problem framing
-   Product requirements
-   Customer value assessment
-   AI product management
-   Evaluation design
-   Responsible AI
-   Risk management
-   Product analytics
-   Launch readiness
-   Go-to-market thinking
-   Executive communication
-   Evidence-based decision making

### Interview Story

A concise way to describe the project:

> **"I built LaunchPilot AI as a product launch decision system for
> AI-enabled products. Instead of treating launch readiness as a
> subjective checklist, I connected product definition, five launch
> gates, AI evaluation, risk management, and executive decision-making
> into one workflow that produces a defensible GO, ITERATE, or NO-GO
> recommendation."**

### Portfolio Note

This is a portfolio project using synthetic demo data. The project should be discussed as a demonstration of **PM thinking, product design, decision frameworks, and implementation ability**, not as evidence of
real company business outcomes.

---

## 👤 Author

**Abhishek Kumar Gond**  
IIT Guwahati 
- **Email : mr.abhishekaaa@gmail.com**
- **[Portfolio]()**
- **[LinkedIn](https://www.linkedin.com/in/abhishekkumargond/)**

---=

## 📄 License

Released under the [MIT License](LICENSE).

---
