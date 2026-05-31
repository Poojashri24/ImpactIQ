from backend.llm_client import call_llm


def impact_agent(change):
    return f"""
You are an enterprise architect.

Analyze IMPACT of this change:
{change}

Return structured business + technical impact.
"""


def risk_agent(change):
    return f"""
You are a risk officer.

Identify risks for:
{change}

Return:
- Operational risks
- Technical risks
- Security risks
- Financial risks
"""


def training_agent(change):
    return f"""
You are a training strategist.

Define training requirements for:
{change}

Return:
- Teams impacted
- Skills required
- Training plan
"""


def scoring_agent(change):
    return f"""
You are a risk scoring engine.

Return ONLY JSON:

{{
  "risk_score": <0-100>,
  "reasons": ["reason1", "reason2", "reason3"]
}}

Change:
{change}
"""