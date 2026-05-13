---
name: "command-equity-research-earnings-preview"
description: "Codex adapter for Claude slash command /earnings-preview from equity-research. Use when the user types /earnings-preview or asks to build a pre-earnings preview with scenarios"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /earnings-preview Command Adapter

Source: `plugins/vertical-plugins/equity-research/commands/earnings-preview.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `earnings-preview` skill and build a pre-earnings analysis with consensus estimates, key metrics to watch, and bull/base/bear scenarios.

If a ticker is provided, use it. Otherwise ask the user which company is reporting.
