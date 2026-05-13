---
name: "command-private-equity-returns"
description: "Codex adapter for Claude slash command /returns from private-equity. Use when the user types /returns or asks to build IRR/MOIC sensitivity tables"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /returns Command Adapter

Source: `plugins/vertical-plugins/private-equity/commands/returns.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `returns-analysis` skill and model PE returns with sensitivity across entry multiple, leverage, exit multiple, and growth scenarios.

If deal parameters are provided, use them. Otherwise ask the user for entry EBITDA, valuation, and financing assumptions.
