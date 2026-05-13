---
name: "command-private-equity-unit-economics"
description: "Codex adapter for Claude slash command /unit-economics from private-equity. Use when the user types /unit-economics or asks to analyze unit economics (ARR cohorts, LTV/CAC, retention)"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /unit-economics Command Adapter

Source: `plugins/vertical-plugins/private-equity/commands/unit-economics.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `unit-economics` skill and analyze customer economics, ARR cohorts, net retention, and revenue quality.

If a company or file is provided, use it. Otherwise ask the user for the target and available data.
