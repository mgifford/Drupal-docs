import json
import os

from intelligence.copilot_client import CopilotClient
from intelligence.gemini_client import GeminiClient
from transformers.md_transformer import OllamaClient


class LLMRouter:
    """
    Local-first model router.

    Policy controls (env vars):
    - LLM_DEFAULT_PROVIDER: ollama|copilot|gemini (default: ollama)
    - LLM_FORCE_PROVIDER: ollama|copilot|gemini (optional per run override)
    - LLM_ENABLE_CLOUD_FALLBACK: true|false (default: true)
    - LLM_TARGET_LOCAL_RATIO: float 0-1 (default: 0.90)
    """

    def __init__(self, stats_file="crawler/content/llm_usage_stats.json"):
        self.stats_file = stats_file
        self.default_provider = os.environ.get("LLM_DEFAULT_PROVIDER", "ollama").lower()
        self.force_provider = os.environ.get("LLM_FORCE_PROVIDER", "").strip().lower() or None
        self.enable_cloud_fallback = os.environ.get("LLM_ENABLE_CLOUD_FALLBACK", "true").lower() == "true"
        self.target_local_ratio = float(os.environ.get("LLM_TARGET_LOCAL_RATIO", "0.90"))

        self.ollama = OllamaClient(
            model=os.environ.get("OLLAMA_MODEL", "qwen2.5-coder:7b"),
            base_url=os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434"),
        )
        self.copilot = CopilotClient()
        self.gemini = GeminiClient(
            model_name=os.environ.get("GEMINI_MODEL", "gemini-1.5-flash")
        )

    def _read_stats(self):
        default = {"local_calls": 0, "cloud_calls": 0, "fallback_calls": 0}
        if not os.path.exists(self.stats_file):
            return default
        try:
            with open(self.stats_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for k in default:
                    if k not in data:
                        data[k] = default[k]
                return data
        except Exception:
            return default

    def _write_stats(self, stats):
        os.makedirs(os.path.dirname(self.stats_file), exist_ok=True)
        with open(self.stats_file, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)

    def _record(self, provider, is_fallback=False):
        stats = self._read_stats()
        if provider == "ollama":
            stats["local_calls"] += 1
        else:
            stats["cloud_calls"] += 1
        if is_fallback:
            stats["fallback_calls"] += 1
        self._write_stats(stats)

    def usage_summary(self):
        stats = self._read_stats()
        total = stats["local_calls"] + stats["cloud_calls"]
        ratio = (stats["local_calls"] / total) if total else 1.0
        return {
            **stats,
            "total_calls": total,
            "local_ratio": round(ratio, 4),
            "meets_target": ratio >= self.target_local_ratio,
            "target_local_ratio": self.target_local_ratio,
        }

    def _cloud_providers(self):
        providers = []
        if self.copilot.available():
            providers.append("copilot")
        if self.gemini.model is not None:
            providers.append("gemini")
        return providers

    def _pick_provider(self, prefer_provider=None):
        if prefer_provider:
            return prefer_provider
        if self.force_provider:
            return self.force_provider
        return self.default_provider

    def _call_provider(self, provider, prompt, system_instruction=None):
        if provider == "ollama":
            return self.ollama.generate(prompt, system_instruction)
        if provider == "copilot":
            return self.copilot.analyze(prompt, system_instruction)
        if provider == "gemini":
            return self.gemini.analyze(prompt, system_instruction)
        raise ValueError(f"Unknown provider: {provider}")

    def _needs_json_array(self, text):
        if not isinstance(text, str):
            return True
        start = text.find("[")
        end = text.rfind("]") + 1
        if start == -1 or end <= start:
            return True
        try:
            parsed = json.loads(text[start:end])
            return not isinstance(parsed, list)
        except Exception:
            return True

    def _needs_json_object(self, text):
        if not isinstance(text, str):
            return True
        start = text.find("{")
        end = text.rfind("}") + 1
        if start == -1 or end <= start:
            return True
        try:
            parsed = json.loads(text[start:end])
            return not isinstance(parsed, dict)
        except Exception:
            return True

    def request(
        self,
        prompt,
        system_instruction=None,
        prefer_provider=None,
        require_json_array=False,
        require_json_object=False,
    ):
        primary = self._pick_provider(prefer_provider=prefer_provider)

        try:
            response = self._call_provider(primary, prompt, system_instruction)
            self._record(primary)

            invalid_json = (
                (require_json_array and self._needs_json_array(response))
                or (require_json_object and self._needs_json_object(response))
            )
            if not invalid_json:
                return response

            if primary != "ollama" or not self.enable_cloud_fallback:
                return response
        except Exception:
            if primary != "ollama" or not self.enable_cloud_fallback:
                raise

        for provider in self._cloud_providers():
            try:
                fallback = self._call_provider(provider, prompt, system_instruction)
                self._record(provider, is_fallback=True)
                return fallback
            except Exception:
                continue

        # Final attempt: bubble up useful local error by retrying local once.
        final = self._call_provider("ollama", prompt, system_instruction)
        self._record("ollama")
        return final

    def generate(self, prompt, system_prompt=None, **kwargs):
        return self.request(prompt, system_instruction=system_prompt, **kwargs)

    def analyze(self, prompt, system_instruction=None, **kwargs):
        return self.request(prompt, system_instruction=system_instruction, **kwargs)
