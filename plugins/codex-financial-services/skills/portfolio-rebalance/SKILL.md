---
name: "portfolio-rebalance"
description: "Codex adapter skill for portfolio-rebalance."
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# Portfolio Rebalance

description: Analyze portfolio allocation drift and generate rebalancing trade recommendations across accounts. Considers tax implications, transaction costs, and wash sale rules. Triggers on "rebalance", "portfolio drift", "allocation check", "rebalancing trades", or "my portfolio is out of balance".

## Workflow

### Step 1: Current State

For each account, capture:
- Account type (taxable, IRA, Roth, 401k)
- Holdings with current market value
- Cost basis (for taxable accounts)
- Unrealized gains/losses per position

### Step 2: Drift Analysis

Compare current allocation to IPS targets:

| Asset Class | Target % | Current % | Drift | $ Over/Under |
|------------|----------|-----------|-------|-------------|
| US Large Cap Equity | | | | |
| US Small/Mid Cap | | | | |
| International Developed | | | | |
| Emerging Markets | | | | |
| Investment Grade Bonds | | | | |
| High Yield / Credit | | | | |
| TIPS / Inflation Protected | | | | |
| Alternatives | | | | |
| Cash | | | | |

Flag positions exceeding the rebalancing band (typically ±3-5%).

### Step 3: Trade Recommendations

Generate trades to bring allocation back to target:

**Tax-Aware Rebalancing Rules:**
- Prefer rebalancing in tax-advantaged accounts (IRA, Roth) first — no tax consequences
- In taxable accounts, avoid selling positions with large short-term gains
- Harvest losses where possible while rebalancing
- Watch for wash sale rules (30-day window) across all accounts
- Consider directing new contributions to underweight asset classes instead of trading

**Trade List:**

| Account | Action | Security | Shares/$ | Reason | Tax Impact |
|---------|--------|----------|----------|--------|-----------|
| | Buy/Sell | | | Rebalance / TLH | ST gain / LT gain / Loss |

### Step 4: Asset Location Review

Optimize which assets are held in which account types:
- **Tax-deferred (IRA/401k)**: Bonds, REITs, high-turnover funds (highest tax drag)
- **Roth**: Highest expected growth assets (tax-free growth)
- **Taxable**: Tax-efficient equity (index funds, ETFs, munis), tax-loss harvesting candidates

### Step 5: Implementation

- Total trades by account
- Estimated transaction costs
- Estimated tax impact (realized gains/losses)
- Net effect on allocation drift

### Step 6: Output

- Drift analysis table
- Recommended trade list (Excel)
- Tax impact summary
- Before/after allocation comparison

## Important Notes

- Don't rebalance for rebalancing's sake — small drift within bands is fine
- Tax costs can outweigh rebalancing benefits in taxable accounts — calculate the breakeven
- Consider pending cash flows (contributions, withdrawals, RMDs) before trading
- Check for any client-specific restrictions (ESG, concentrated stock, lockups)
- Document rationale for every trade for compliance records
- Wash sale rules apply across accounts — coordinate trades across the household
