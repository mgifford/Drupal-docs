import json
import time
from pathlib import Path

import requests


def filename_for_url(url):
    return url.replace("https://", "").replace("/", "_").replace(".", "_") + ".html"


def main():
    repo_root = Path(__file__).resolve().parents[2]
    quality_path = repo_root / "crawler" / "content" / "quality_issues.json"
    state_path = repo_root / "crawler" / "content" / "sync_state.json"
    out_dir = repo_root / "crawler" / "downloads"
    out_dir.mkdir(parents=True, exist_ok=True)

    quality = json.loads(quality_path.read_text(encoding="utf-8")) if quality_path.exists() else []
    state = json.loads(state_path.read_text(encoding="utf-8"))

    file_to_url = {filename_for_url(url): url for url in state.keys()}

    targets = []
    for item in quality:
        name = Path(item["html_file"]).name
        url = file_to_url.get(name)
        if url:
            targets.append((name, url))

    extra_url = "https://www.drupal.org/docs/drupal-apis/update-api/writing-automated-update-tests-for-drupal-8-or-later"
    extra_name = filename_for_url(extra_url)
    if extra_name not in [name for name, _ in targets]:
        targets.append((extra_name, extra_url))

    # Keep conservative fetch behavior to avoid stressing Drupal.org.
    print(f"refresh_targets={len(targets)}")
    for idx, (name, url) in enumerate(targets, start=1):
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        (out_dir / name).write_text(response.text, encoding="utf-8")
        print(f"[{idx}/{len(targets)}] refreshed {name}")
        if idx < len(targets):
            time.sleep(10)

    print("refresh_complete=true")


if __name__ == "__main__":
    main()
