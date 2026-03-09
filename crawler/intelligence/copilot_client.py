import os
import requests


class CopilotClient:
    """Calls GitHub Models (Copilot-backed) via OpenAI-compatible chat API."""

    def __init__(self, token=None, model_name=None, base_url=None, timeout=120):
        self.token = token or os.environ.get("GITHUB_TOKEN")
        self.model_name = model_name or os.environ.get("COPILOT_MODEL", "gpt-4.1-mini")
        self.base_url = base_url or os.environ.get(
            "COPILOT_BASE_URL",
            "https://models.inference.ai.azure.com/chat/completions",
        )
        self.timeout = timeout

    def available(self):
        return bool(self.token)

    def analyze(self, prompt, system_instruction=None):
        if not self.available():
            raise RuntimeError("Copilot client is unavailable: missing GITHUB_TOKEN")

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model_name,
            "messages": messages,
            "temperature": 0.2,
        }

        response = requests.post(
            self.base_url,
            headers=headers,
            json=payload,
            timeout=self.timeout,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
