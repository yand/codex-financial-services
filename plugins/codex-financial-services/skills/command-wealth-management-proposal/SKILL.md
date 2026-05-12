---
name: "command-wealth-management-proposal"
description: "Codex adapter for Claude slash command /proposal from wealth-management. Use when the user types /proposal or asks to create an investment proposal for a prospect"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /proposal Command Adapter

Source: `plugins/vertical-plugins/wealth-management/commands/proposal.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `investment-proposal` skill to create a personalized investment proposal for a prospective client.

If a prospect name is provided, use it. Otherwise ask for prospect details.
