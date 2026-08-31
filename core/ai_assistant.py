"""Optional AI layer.

The application works without an API key. If OPENAI_API_KEY is configured,
this module can be extended to call an LLM. The default deterministic engine is
used in the portfolio demo so deployment remains reproducible and cost-free.
"""


def generate_product_questions(problem: str, persona: str) -> list[str]:
    return [
        f"What evidence proves that {persona} experiences this problem frequently?",
        "Which user behavior would indicate the product is solving the problem rather than adding another workflow?",
        "What is the smallest MVP that can validate the core value proposition?",
        "What AI failure would create the highest customer or trust impact?",
        "What guardrail would prevent a misleading or overconfident AI response?",
        "What metric would make us stop, iterate, or scale the launch?",
    ]
