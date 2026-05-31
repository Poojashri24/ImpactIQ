import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

API_KEY = st.secrets["OPENROUTER_API_KEY"]


def call_llm(prompt, model="openai/gpt-4o-mini"):

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.3
            },
            timeout=60
        )

        if response.status_code != 200:
            return f"API Error: {response.text}"

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:

        return f"LLM Error: {str(e)}"