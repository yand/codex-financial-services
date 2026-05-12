---
name: "command-lseg-analyze-bond-basis"
description: "Codex adapter for Claude slash command /analyze-bond-basis from lseg. Use when the user types /analyze-bond-basis or asks to analyze the bond futures basis with CTD identification, implied repo rate, and basis trade assessment"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /analyze-bond-basis Command Adapter

Source: `plugins/partner-built/lseg/commands/analyze-bond-basis.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

# Analyze Bond Futures Basis

> This command uses LSEG bond future pricing, bond pricing, yield curves, and historical data tools. See [CONNECTORS.md](../CONNECTORS.md) for available tools.

Analyze the bond futures basis by pricing the future, identifying the cheapest-to-deliver bond, computing gross and net basis, and assessing basis trade opportunities.

See the **bond-futures-basis** skill for domain knowledge on basis mechanics and trading strategies.

## Workflow

### 1. Gather Input

Ask the user for:
- Bond future RIC (required) — e.g., FGBLc1 (Euro Bund), TYc1 (US 10Y Note), FFIc1 (UK Gilt)
- Market data date (optional, defaults to today)

### 2. Price the Bond Future

Call `bond_future_price` with the future RIC.

Extract: fair price, CTD bond identifier, delivery basket with conversion factors, contract DV01, delivery dates.

### 3. Price the CTD Bond

Call `bond_price` for the CTD identifier from Step 2.

Extract: clean/dirty price, yield, duration, DV01, accrued interest, coupon.

Compute: gross basis, invoice price, carry, net basis.

### 4. Compute Implied Repo Rate

Call `interest_rate_curve` (list then calculate) for the future's currency. Use short-end rate as repo proxy.

Compute implied repo rate and compare to market repo.

### 5. Track Historical Basis

Call `tscc_historical_pricing_summaries` for both the future and CTD bond with `tenor: "3M"`, `interval: "P1D"`.

Assess: basis trend, volatility, and historical range.

### 6. Sovereign Credit Context

Call `credit_curve` for the relevant sovereign (e.g., "DE" for Bund, "US" for Treasury).

### 7. Synthesize the Report

Present: future summary table, CTD bond analytics, basis calculation table (gross/net basis, implied repo vs market repo), historical context, and trade recommendation (long basis / short basis / neutral).

## Output Format

Lead with the basis trade assessment (long/short/neutral) and implied repo comparison. Follow with detailed analytics tables.
