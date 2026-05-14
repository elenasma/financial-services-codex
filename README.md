# Financial Services for Codex

Codex-compatible adaptation of Anthropic's open source `financial-services` plugin repository.

This repository keeps the upstream financial-services skills, commands, hooks, and MCP connector declarations, and adds Codex plugin manifests so other Codex users can install the bundles from a marketplace-style repo.

> Important: Nothing in this repository constitutes investment, legal, tax, or accounting advice. These workflows draft analyst work product for review by qualified professionals. Users are responsible for verification, compliance, and provider credentials.

## What Changed For Codex

- Added `.codex-plugin/plugin.json` manifests for each plugin under `plugins/`.
- Added `.agents/plugins/marketplace.json` so Codex can discover the plugin catalog from this repo.
- Preserved upstream `.claude-plugin/plugin.json` files for traceability.
- Preserved upstream `.mcp.json` connector declarations and exposed them through the Codex `mcpServers` manifest field.
- Preserved upstream `commands/`, `hooks/`, `skills/`, and managed-agent cookbook files.

## Install In Codex

Use this repository as a Codex plugin marketplace/source. Install the specific plugins you need from the catalog, starting with `financial-analysis` for shared modeling and data-connector declarations.

From a local checkout, register this repository with Codex and enable the shared core plugin:

```bash
python3 scripts/register-local-marketplace.py
```

The script updates `~/.codex/config.toml` idempotently with:

```toml
[plugins."financial-analysis@financial-services-codex"]
enabled = true

[marketplaces.financial-services-codex]
source_type = "local"
source = "/path/to/financial-services-codex"
```

Restart Codex after registering the marketplace so the newly enabled plugin is loaded. Other plugins in this marketplace can then be enabled from the catalog as needed.

Recommended first installs:

- `financial-analysis`: DCF, comps, LBO, 3-statement models, Excel audit, deck QC, and shared MCP connector declarations.
- `investment-banking`: CIMs, teasers, buyer lists, merger models, process letters, and deal tracking.
- `equity-research`: earnings analysis, initiations, model updates, thesis tracking, and catalyst calendars.
- `private-equity`: deal sourcing, screening, IC memos, diligence, portfolio monitoring, and returns analysis.
- `wealth-management`: client reviews, plans, proposals, rebalancing, tax-loss harvesting, and reporting.
- `fund-admin`: GL recon, NAV tie-out, accrual schedules, roll-forwards, and variance commentary.
- `operations`: KYC document parsing and rules-grid workflows.

## MCP Connectors

Several plugins reference external MCP servers through `.mcp.json`. These declarations are preserved, but data access depends on your local Codex MCP support and your credentials/subscriptions with providers such as Daloopa, Morningstar, FactSet, PitchBook, LSEG, and S&P Global.

The skills remain useful as workflow guidance without those connectors, but connector-backed market, company, and filing data will require separate setup.

## Upstream

Original project: https://github.com/anthropics/financial-services

The original README is preserved in `README.anthropic.md`.

## License

This adaptation preserves the upstream MIT license. See `LICENSE`.
