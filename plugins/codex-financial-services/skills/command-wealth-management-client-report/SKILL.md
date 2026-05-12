---
name: "command-wealth-management-client-report"
description: "Codex adapter for Claude slash command /client-report from wealth-management. Use when the user types /client-report or asks to generate a client performance report"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /client-report Command Adapter

Source: `plugins/vertical-plugins/wealth-management/commands/client-report.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `client-report` skill to generate a professional client-facing performance report.

If a client and period are provided, use them. Otherwise ask for client details and reporting period.
