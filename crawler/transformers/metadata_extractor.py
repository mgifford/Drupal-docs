import json

class MetadataExtractor:
    def __init__(self, ollama_client):
        self.client = ollama_client

    def extract(self, html_content):
        system_prompt = "Extract semantic metadata from the provided HTML. Look for RDFa, Microformats, or common Drupal metadata patterns. Output ONLY a JSON object with fields: title, source_url, author, last_updated, tags, summary."
        prompt = f"Extract metadata from this HTML:\n\n{html_content}"
        
        response_text = self.client.generate(prompt, system_prompt)
        try:
            # Attempt to find JSON in the response if the model adds flavor text
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start != -1 and end != -1:
                return json.loads(response_text[start:end])
            return json.loads(response_text)
        except Exception:
            return {"error": "Failed to parse metadata", "raw": response_text}
