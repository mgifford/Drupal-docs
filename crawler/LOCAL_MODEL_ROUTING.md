# Local-First Model Routing

This project is configured to run **local Ollama by default** with optional cloud fallback.

## Goals
- Keep at least 90% of LLM calls local.
- Allow explicit provider switches (for troubleshooting or quality checks).
- Fallback to Copilot/GitHub Models automatically only when local fails or returns invalid JSON for structured tasks.

## Cost Policy (Local-First)
- Default to local Ollama for all crawl/sync processing.
- Use cloud models only by explicit request or strict fallback conditions.
- Keep cloud usage at or below 10% of total model calls.
- For routine conversion batches, run strict local-only mode.

## 1. Configure environment
Copy `crawler/.env.example` to your local env file and set real values.

Important variables:
- `LLM_DEFAULT_PROVIDER=ollama`
- `LLM_TARGET_LOCAL_RATIO=0.90`
- `LLM_ENABLE_CLOUD_FALLBACK=true`
- `OLLAMA_BASE_URL`, `OLLAMA_MODEL`
- `GITHUB_TOKEN`, `COPILOT_MODEL` (for Copilot fallback)

## 2. Run local-first (default)
```bash
python crawler/main.py --sync
```

## 2a. Run strict local-only for batch conversion
```bash
python crawler/main.py --sync --llm-provider ollama --no-cloud-fallback
```

Use this for normal Drupal.org conversion to avoid paid model usage.

## 3. Force provider on request
Use one-run override flags:

```bash
python crawler/main.py --sync --llm-provider ollama
python crawler/main.py --sync --llm-provider copilot
python crawler/main.py --sync --llm-provider gemini
```

## 4. Disable cloud fallback (strict local-only)
```bash
python crawler/main.py --sync --no-cloud-fallback
```

## 5. Verify local/cloud ratio
The router writes usage metrics to:
- `crawler/content/llm_usage_stats.json`

Fields:
- `local_calls`
- `cloud_calls`
- `fallback_calls`

Keep `local_calls / (local_calls + cloud_calls) >= 0.90` to satisfy your target.

Example current run (March 2026):
- `local_calls: 294`
- `cloud_calls: 0`
- `fallback_calls: 0`

This equals 100% local usage so far.

## 6. Audit Prompt Volume and Quality
- Prompt log (ignored from git): `crawler/content/ollama_prompts.log.md`
- Current-run quality skips: `crawler/content/quality_issues.json`

Quick checks:
```bash
grep -R -l 'Discover Drupal' content/docs | wc -l
grep -R -l '```markdown' content/docs | wc -l
cat crawler/content/llm_usage_stats.json
```

## Notes
- Structured tasks (metadata extraction and gap analysis) trigger cloud fallback only when local output is invalid JSON and cloud fallback is enabled.
- Cloud fallback checks Copilot first (if `GITHUB_TOKEN` is present), then Gemini (if `GEMINI_API_KEY` is present).
