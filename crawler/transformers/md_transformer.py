import requests
import json

class OllamaClient:
    def __init__(self, model="qwen2.5-coder:7b", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = f"{base_url}/api/generate"

    def generate(self, prompt, system_prompt=None):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        if system_prompt:
            payload["system"] = system_prompt
            
        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")

class MarkdownTransformer:
    def __init__(self, ollama_client=None):
        self.client = ollama_client or OllamaClient()

    def transform(self, html_content):
        system_prompt = "You are a specialized HTML-to-Markdown transformer. Convert the provided HTML to clean, idiomatic Markdown. Preserve headings, lists, and code blocks. Strip any navigation or sidebar boilerplate."
        prompt = f"Convert this HTML to Markdown:\n\n{html_content}"
        
        return self.client.generate(prompt, system_prompt)
