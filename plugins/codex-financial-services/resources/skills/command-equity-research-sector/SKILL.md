---
name: "command-equity-research-sector"
description: "Codex adapter for Claude slash command /sector from equity-research. Use when the user types /sector or asks to create a sector overview report"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /sector Command Adapter

Source: `plugins/vertical-plugins/equity-research/commands/sector.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `sector-overview` skill and create an industry landscape report covering market sizing, competitive dynamics, and investment implications.

If a sector is provided, use it. Otherwise ask the user which industry to cover.
