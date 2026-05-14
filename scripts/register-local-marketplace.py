#!/usr/bin/env python3
"""Register this checkout as a local Codex plugin marketplace."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = Path.home() / ".codex" / "config.toml"
MARKETPLACE_NAME = "financial-services-codex"
PLUGIN_NAME = "financial-analysis@financial-services-codex"


def block_present(text: str, header: str) -> bool:
    return f"[{header}]" in text


def main() -> None:
    text = CONFIG.read_text(encoding="utf-8") if CONFIG.exists() else ""
    additions: list[str] = []

    if not block_present(text, f'plugins."{PLUGIN_NAME}"'):
        additions.append(
            "\n"
            f'[plugins."{PLUGIN_NAME}"]\n'
            "enabled = true\n"
        )

    if not block_present(text, f"marketplaces.{MARKETPLACE_NAME}"):
        now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        additions.append(
            "\n"
            f"[marketplaces.{MARKETPLACE_NAME}]\n"
            f'last_updated = "{now}"\n'
            'source_type = "local"\n'
            f'source = "{ROOT}"\n'
        )

    if additions:
        CONFIG.parent.mkdir(parents=True, exist_ok=True)
        CONFIG.write_text(text.rstrip() + "\n" + "".join(additions), encoding="utf-8")
        print(f"Updated {CONFIG}")
        print(f"Enabled {PLUGIN_NAME}")
        print(f"Registered marketplace {MARKETPLACE_NAME} -> {ROOT}")
    else:
        print(f"No changes needed in {CONFIG}")

    print("Restart Codex to pick up newly enabled plugins.")


if __name__ == "__main__":
    main()
