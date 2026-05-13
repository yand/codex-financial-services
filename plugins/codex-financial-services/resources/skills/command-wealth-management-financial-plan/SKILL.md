---
name: "command-wealth-management-financial-plan"
description: "Codex adapter for Claude slash command /financial-plan from wealth-management. Use when the user types /financial-plan or asks to build or update a financial plan"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /financial-plan Command Adapter

Source: `plugins/vertical-plugins/wealth-management/commands/financial-plan.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `financial-plan` skill to create or update a comprehensive financial plan covering retirement, education, estate, and cash flow projections.

If a client name is provided, use it. Otherwise ask for client details.
