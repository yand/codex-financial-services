---
name: "command-equity-research-initiate"
description: "Codex adapter for Claude slash command /initiate from equity-research. Use when the user types /initiate or asks to create an initiating coverage report"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /initiate Command Adapter

Source: `plugins/vertical-plugins/equity-research/commands/initiate.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `initiating-coverage` skill and begin the 5-task workflow to create an institutional-quality initiation report.

If a ticker is provided, use it. Otherwise ask the user which company to initiate on.
