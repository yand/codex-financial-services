---
name: "command-investment-banking-deal-tracker"
description: "Codex adapter for Claude slash command /deal-tracker from investment-banking. Use when the user types /deal-tracker or asks to track and review live deal pipeline"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /deal-tracker Command Adapter

Source: `plugins/vertical-plugins/investment-banking/commands/deal-tracker.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `deal-tracker` skill to review deal status, update milestones, and manage action items across live deals.
