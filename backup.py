import requests

from config import GROQ_BASE_URL, GROQ_API_KEY


class LLMService:
    def __init__(self):
        self.groq_endpoint = GROQ_BASE_URL
        self.api_key = GROQ_API_KEY

    def query_llm(self, prompt: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            "temperature": 0.7,

        }
        
        response = requests.post(self.groq_endpoint, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
