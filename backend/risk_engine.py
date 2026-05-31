import json


def risk_level(score):

    if score >= 70:
        return "High"

    elif score >= 40:
        return "Medium"

    return "Low"


def compute_risk(llm_output):

    try:

        data = json.loads(llm_output)

        score = int(data.get("risk_score", 50))

        reasons = data.get("reasons", [])

    except:

        score = 50

        reasons = []

    return {
        "risk_score": score,
        "risk_level": risk_level(score),
        "reasons": reasons
    }