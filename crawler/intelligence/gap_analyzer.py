import json
from intelligence.gemini_client import GeminiClient

class GapAnalyzer:
    def __init__(self, gemini_client=None):
        self.client = gemini_client or GeminiClient()

    def analyze_gaps(self, markdown_content, target_version="Drupal 11"):
        system_instruction = f"You are a Drupal documentation auditor. Compare the provided documentation against your knowledge of {target_version}. Identify missing sections, outdated instructions (especially D7/D9 legacy), or incorrect technical details. Output ONLY a JSON list of objects with fields: 'severity' (Low/Medium/High), 'issue', 'recommendation'."
        
        prompt = f"Audit this documentation for {target_version} readiness:\n\n{markdown_content}"
        
        response_text = self.client.analyze(prompt, system_instruction)
        try:
            # Extract JSON from response
            start = response_text.find('[')
            end = response_text.rfind(']') + 1
            if start != -1 and end != -1:
                return json.loads(response_text[start:end])
            return json.loads(response_text)
        except Exception:
            return [{"severity": "High", "issue": "Failed to parse analysis", "recommendation": "Manual review required"}]
