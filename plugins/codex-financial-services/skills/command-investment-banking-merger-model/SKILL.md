---
name: "command-investment-banking-merger-model"
description: "Codex adapter for Claude slash command /merger-model from investment-banking. Use when the user types /merger-model or asks to build an accretion/dilution merger model"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /merger-model Command Adapter

Source: `plugins/vertical-plugins/investment-banking/commands/merger-model.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `merger-model` skill and build a merger consequences analysis.

If acquirer and target are provided, use them. Otherwise ask the user for deal details.
