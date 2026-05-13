---
name: "command-equity-research-catalysts"
description: "Codex adapter for Claude slash command /catalysts from equity-research. Use when the user types /catalysts or asks to view or update the catalyst calendar"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /catalysts Command Adapter

Source: `plugins/vertical-plugins/equity-research/commands/catalysts.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `catalyst-calendar` skill to build or review upcoming catalysts across the coverage universe.

If a timeframe is provided, use it. Otherwise default to the next 2 weeks.
