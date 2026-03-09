import requests
import json
import os
import re
from datetime import datetime, timezone

class OllamaClient:
    def __init__(self, model="qwen2.5-coder:7b", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = f"{base_url}/api/generate"
        self.prompt_logging_enabled = os.environ.get("OLLAMA_PROMPT_LOGGING", "true").lower() == "true"
        self.prompt_log_file = self._resolve_prompt_log_file()

    def _resolve_prompt_log_file(self):
        configured = os.environ.get("OLLAMA_PROMPT_LOG_FILE", "").strip()
        if configured:
            if os.path.isabs(configured):
                return configured

            repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            return os.path.join(repo_root, configured)

        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        return os.path.join(repo_root, "crawler", "content", "ollama_prompts.log.md")

    def _append_prompt_log(self, prompt, system_prompt=None):
        if not self.prompt_logging_enabled:
            return

        os.makedirs(os.path.dirname(self.prompt_log_file), exist_ok=True)
        timestamp = datetime.now(timezone.utc).isoformat()
        system_text = system_prompt if system_prompt else ""

        with open(self.prompt_log_file, "a", encoding="utf-8") as f:
            f.write(f"## {timestamp} | model={self.model}\n\n")
            f.write(f"- prompt_chars: {len(prompt)}\n")
            f.write(f"- system_chars: {len(system_text)}\n\n")
            f.write("### System Prompt\n\n")
            f.write("```text\n")
            f.write(system_text)
            f.write("\n```\n\n")
            f.write("### Prompt\n\n")
            f.write("```text\n")
            f.write(prompt)
            f.write("\n```\n\n")

    def generate(self, prompt, system_prompt=None):
        self._append_prompt_log(prompt, system_prompt)
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

    def strip_outer_markdown_fence(self, text):
        if not isinstance(text, str):
            return text

        stripped = text.strip()
        match = re.match(r"^```(?:markdown|md)?\n([\s\S]*?)\n```$", stripped, flags=re.IGNORECASE)
        if match:
            return match.group(1).strip() + "\n"
        return text

    def looks_like_homepage_boilerplate(self, markdown_text):
        if not markdown_text:
            return False

        probe = markdown_text.lower()
        required_markers = [
            "discover drupal",
            "build with drupal",
            "partners & services",
            "support drupal",
            "drupal core",
            "drupal cms",
        ]
        return sum(1 for marker in required_markers if marker in probe) >= 5

    def transform(self, html_content):
        system_prompt = (
            "You are a specialized HTML-to-Markdown transformer. Convert only the page's main article "
            "content into clean Markdown. Exclude global site navigation, footer menus, partner links, and "
            "homepage marketing blocks. Do not wrap output in ```markdown fences."
        )
        prompt = f"Convert this HTML to Markdown:\n\n{html_content}"

        first_pass = self.client.generate(prompt, system_prompt)
        first_pass = self.strip_outer_markdown_fence(first_pass)
        if not self.looks_like_homepage_boilerplate(first_pass):
            return first_pass

        retry_system_prompt = (
            "You are cleaning a bad extraction. Output only task-specific documentation body text and headings. "
            "Drop any sections titled Discover Drupal, Build with Drupal, Community, Support Drupal, or similar "
            "global navigation sections. Do not wrap output in markdown code fences."
        )
        retry = self.client.generate(prompt, retry_system_prompt)
        return self.strip_outer_markdown_fence(retry)
