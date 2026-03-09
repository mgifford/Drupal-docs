import os
from intelligence.llm_router import LLMRouter
from intelligence.ai_merger import AIMerger
from intelligence.gap_analyzer import GapAnalyzer

class IntelligenceOrchestrator:
    def __init__(self):
        self.client = LLMRouter()
        self.merger = AIMerger(self.client)
        self.gap_analyzer = GapAnalyzer(self.client)

    def process_content(self, markdown_path):
        with open(markdown_path, 'r') as f:
            content = f.read()

        # 1. Analyze Gaps
        print(f"Analyzing gaps for: {markdown_path}")
        gaps = self.gap_analyzer.analyze_gaps(content)
        
        # 2. In a real scenario, if source B exists, we'd merge. 
        # For this WP, we focus on the Intelligence layer capabilities.
        
        return {
            "file": markdown_path,
            "gaps": gaps
        }

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        orch = IntelligenceOrchestrator()
        result = orch.process_content(sys.argv[1])
        print(result)
    else:
        print("Usage: python intelligence/orchestrator.py <markdown_path>")
