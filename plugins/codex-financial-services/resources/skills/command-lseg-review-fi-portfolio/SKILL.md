---
name: "command-lseg-review-fi-portfolio"
description: "Codex adapter for Claude slash command /review-fi-portfolio from lseg. Use when the user types /review-fi-portfolio or asks to review a fixed income portfolio with pricing, reference data, cashflows, and scenario analysis"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /review-fi-portfolio Command Adapter

Source: `plugins/partner-built/lseg/commands/review-fi-portfolio.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

# Review Fixed Income Portfolio

> This command uses LSEG bond pricing, YieldBook analytics, and yield curve tools. See [CONNECTORS.md](../CONNECTORS.md) for available tools.

Produce a consolidated fixed income portfolio risk and return report by pricing all holdings, enriching with reference data, projecting cashflows, and stress testing under rate scenarios.

See the **fixed-income-portfolio** skill for domain knowledge on portfolio analytics and scenario analysis.

## Workflow

### 1. Gather Portfolio Holdings

Ask the user for:
- Bond identifiers (required) — comma-separated ISINs, CUSIPs, or RICs
- Position sizes/weights (optional — if not provided, assume equal weight)
- Specific scenario to test (optional — e.g., "+100bp", defaults to standard grid)
- Valuation date (optional, defaults to today)

### 2. Price All Bonds

Call `bond_price` with all identifiers.

Extract per bond: clean/dirty price, yield, duration, convexity, DV01, currency.

Aggregate portfolio-level: weighted yield, weighted duration, total DV01, total market value.

### 3. Enrich with Reference Data

Call `yieldbook_bond_reference` for each bond.

Extract: security type, sector, ratings, coupon type, call features, issuer, country.

Build composition breakdowns: by sector, rating, maturity bucket, currency.

### 4. Project Cashflows

Call `yieldbook_cashflow` for each bond.

Aggregate into quarterly cashflow waterfall. Flag periods with concentrated maturities.

### 5. Run Scenario Analysis

Call `yieldbook_scenario` with rate shifts: -200bp, -100bp, -50bp, 0bp, +50bp, +100bp, +200bp.

Identify which bonds contribute most to upside and downside risk.

### 6. Curve Context

Call `interest_rate_curve` for the portfolio's primary currency.

Compute spread to curve for each bond. Assess curve environment.

### 7. Synthesize the Report

Present: portfolio summary metrics, composition breakdowns, cashflow waterfall, scenario P&L table with risk contributors, and curve exposure.

## Output Format

Lead with the portfolio summary metrics, then detail composition, cashflows, and risk analysis in sections.
