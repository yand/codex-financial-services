---
name: "command-private-equity-portfolio"
description: "Codex adapter for Claude slash command /portfolio from private-equity. Use when the user types /portfolio or asks to review portfolio company performance"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /portfolio Command Adapter

Source: `plugins/vertical-plugins/private-equity/commands/portfolio.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `portfolio-monitoring` skill and analyze a portfolio company's performance against plan — KPIs, variances, and red flags.

If a company name or file is provided, use it. Otherwise ask the user for the portfolio company and financial data.
