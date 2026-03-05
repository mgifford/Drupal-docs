import os
import google.generativeai as genai

class GeminiClient:
    def __init__(self, api_key=None, model_name="gemini-1.5-flash"):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            print("Warning: GEMINI_API_KEY not found. Gemini features will be disabled.")
            self.model = None
            return
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    def analyze(self, prompt, system_instruction=None):
        if not self.model:
            return "Gemini is disabled (missing API key)."
            
        if system_instruction:
            # Re-initializing with system instruction if provided
            model = genai.GenerativeModel(
                model_name=self.model.model_name,
                system_instruction=system_instruction
            )
        else:
            model = self.model
            
        response = model.generate_content(prompt)
        return response.text
