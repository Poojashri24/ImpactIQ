from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
API_KEY = os.getenv("OPENROUTER_API_KEY")


class Request(BaseModel):
    change: str


def call_ai(prompt):
    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "openai/gpt-oss-20b",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        return res.json()["choices"][0]["message"]["content"]
    except:
        return "error"


@app.post("/analyze")
def analyze(req: Request):

    change = req.change

    impact = call_ai(f"Impact analysis: {change}")
    risk = call_ai(f"Risk analysis: {change}")
    training = call_ai(f"Training needed: {change}")

    score_raw = call_ai(f"""
Return ONLY JSON:
{{
"risk_score": 0-100,
"confidence": 0-1,
"reasons": []
}}

Change:
{change}
""")

    try:
        score = json.loads(score_raw)
    except:
        score = {"risk_score": 50, "confidence": 0.5, "reasons": []}

    return {
        "impact": impact,
        "risk": risk,
        "training": training,
        "score": score
    }