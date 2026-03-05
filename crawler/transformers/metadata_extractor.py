import json
import re

class MetadataExtractor:
    def __init__(self, ollama_client):
        self.client = ollama_client

    def extract(self, html_content):
        system_prompt = (
            "Extract semantic metadata from the provided HTML. "
            "Look for RDFa, Microformats, or common Drupal metadata patterns. "
            "Output ONLY a JSON object with fields: "
            "title, source_url, author, last_updated, tags, summary, drupal_version, themes."
        )
        prompt = f"Extract metadata from this HTML:\n\n{html_content}"
        
        response_text = self.client.generate(prompt, system_prompt)
        metadata = {}
        try:
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start != -1 and end != -1:
                metadata = json.loads(response_text[start:end])
            else:
                metadata = json.loads(response_text)
        except Exception:
            metadata = {"error": "Failed to parse metadata", "raw": response_text}

        # Add readability score
        metadata['readability_score'] = self.calculate_readability(html_content)
        return metadata

    def calculate_readability(self, html):
        # Strip tags for a crude text extraction
        text = re.sub('<[^<]+?>', '', html)
        words = re.findall(r'\w+', text)
        sentences = re.split(r'[.!?]+', text)
        
        word_count = len(words)
        sentence_count = max(len(sentences), 1)
        
        if word_count == 0:
            return 0
            
        syllable_count = sum(self.count_syllables(w) for w in words)
        
        # Flesch Reading Ease Formula
        score = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllable_count / word_count)
        return round(score, 2)

    def count_syllables(self, word):
        word = word.lower()
        if not word: return 0
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        return count
