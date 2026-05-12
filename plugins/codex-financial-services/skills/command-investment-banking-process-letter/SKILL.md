---
name: "command-investment-banking-process-letter"
description: "Codex adapter for Claude slash command /process-letter from investment-banking. Use when the user types /process-letter or asks to draft a process letter or bid instructions"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /process-letter Command Adapter

Source: `plugins/vertical-plugins/investment-banking/commands/process-letter.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `process-letter` skill and draft process correspondence.

If a letter type is specified (IOI, final bid, management meeting invite), use it. Otherwise ask the user what stage the process is in.
