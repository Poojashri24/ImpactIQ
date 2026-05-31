import json
import re
from backend.llm_client import call_llm


def generate_dependency_graph(change):

    prompt = f"""
You are an Enterprise Architecture Expert.

Analyze the following change request and identify:

1. Impacted enterprise systems
2. Dependencies between systems

Return ONLY valid JSON.

Example:

{{
  "nodes": [
    "Frontend",
    "Database",
    "QA Team"
  ],
  "relationships": [
    ["Frontend", "Database"],
    ["Frontend", "QA Team"]
  ]
}}

Change Request:
{change}
"""

    response = call_llm(prompt)

    print("\n========== GRAPH RESPONSE ==========")
    print(response)
    print("====================================\n")

    try:

        # Extract JSON if model wraps it with text
        match = re.search(r"\{.*\}", response, re.DOTALL)

        if match:
            json_text = match.group()
            return json.loads(json_text)

    except Exception as e:
        print("GRAPH ERROR:", e)

    return {
        "nodes": [
            "Analysis Failed"
        ],
        "relationships": []
    }