---
name: "command-wealth-management-tlh"
description: "Codex adapter for Claude slash command /tlh from wealth-management. Use when the user types /tlh or asks to identify tax-loss harvesting opportunities"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /tlh Command Adapter

Source: `plugins/vertical-plugins/wealth-management/commands/tlh.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `tax-loss-harvesting` skill to scan taxable accounts for harvestable losses, suggest replacement securities, and manage wash sale windows.

If a client or account is provided, use it. Otherwise ask for the portfolio to scan.
