---
name: "command-equity-research-model-update"
description: "Codex adapter for Claude slash command /model-update from equity-research. Use when the user types /model-update or asks to update a financial model with new data"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /model-update Command Adapter

Source: `plugins/vertical-plugins/equity-research/commands/model-update.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `model-update` skill and plug in new earnings, guidance, or revised assumptions.

If a ticker is provided, use it. Otherwise ask the user which model to update and what changed.
