---
name: "command-lseg-analyze-bond-rv"
description: "Codex adapter for Claude slash command /analyze-bond-rv from lseg. Use when the user types /analyze-bond-rv or asks to analyze a bond's relative value vs yield curves and credit spreads with scenario stress testing"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /analyze-bond-rv Command Adapter

Source: `plugins/partner-built/lseg/commands/analyze-bond-rv.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

# Analyze Bond Relative Value

> This command uses LSEG bond pricing, yield curves, credit curves, and scenario analysis tools. See [CONNECTORS.md](../CONNECTORS.md) for available tools.

Perform relative value analysis on one or more bonds by combining pricing analytics, yield curve context, credit spread decomposition, and rate shock scenarios.

See the **bond-relative-value** skill for domain knowledge on spread frameworks and rich/cheap assessment.

## Workflow

### 1. Gather Bond Identifiers

Ask the user for:
- Bond identifier(s) — ISIN, RIC, or CUSIP (required)
- Optional benchmark bond for comparison
- Valuation date (optional, defaults to today)

### 2. Price the Bond(s)

Call `bond_price` with the identifier(s).

Extract: clean/dirty price, yield, duration, convexity, DV01, currency.

If benchmark provided, price that too.

### 3. Get the Risk-Free Yield Curve

Call `interest_rate_curve` (list then calculate) for the bond's currency.

Interpolate at the bond's maturity to compute G-spread.

### 4. Get the Credit Spread Curve

Call `credit_curve` (search by country/issuerType, then calculate).

Compute residual spread = bond G-spread minus credit curve spread at matching maturity. Positive residual = cheap; negative = rich.

### 5. Run Scenario Analysis

Call `yieldbook_scenario` with parallel rate shifts: -100bp, -50bp, 0bp, +50bp, +100bp.

Extract price change and P&L under each scenario.

### 6. Synthesize the Report

Present: bond summary table, spread decomposition (G-spread, credit spread, residual), scenario P&L table, and rich/cheap assessment.

If benchmark provided, include side-by-side comparison.

## Output Format

Lead with the rich/cheap assessment and supporting evidence. Follow with spread decomposition and scenario tables.
