---
name: "command-investment-banking-buyer-list"
description: "Codex adapter for Claude slash command /buyer-list from investment-banking. Use when the user types /buyer-list or asks to build a buyer universe for a sell-side process"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /buyer-list Command Adapter

Source: `plugins/vertical-plugins/investment-banking/commands/buyer-list.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `buyer-list` skill and build a universe of potential strategic and financial acquirers.

If a company or sector is provided, use it. Otherwise ask the user for the target company details.
