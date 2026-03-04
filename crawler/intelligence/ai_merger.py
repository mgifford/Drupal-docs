from intelligence.gemini_client import GeminiClient

class AIMerger:
    def __init__(self, gemini_client=None):
        self.client = gemini_client or GeminiClient()

    def merge_content(self, source_a_md, source_b_md, context="Drupal 11"):
        system_instruction = f"You are an expert Drupal documentation architect. Your task is to merge two documentation sources into one definitive, high-quality Markdown file for {context}. Eliminate redundancy, ensure technical accuracy, and prioritize the most recent information (Drupal CMS/Drupal 11). Preserve formatting and code blocks."
        
        prompt = f"""
        Merge the following two documentation sources:
        
        SOURCE A (Drupal.org Mirror):
        {source_a_md}
        
        SOURCE B (Drupal CMS / Secondary):
        {source_b_md}
        
        OUTPUT: One consolidated Markdown file.
        """
        
        return self.client.analyze(prompt, system_instruction)
