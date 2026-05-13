---
name: "command-equity-research-morning-note"
description: "Codex adapter for Claude slash command /morning-note from equity-research. Use when the user types /morning-note or asks to draft a morning meeting note"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /morning-note Command Adapter

Source: `plugins/vertical-plugins/equity-research/commands/morning-note.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `morning-note` skill and draft a concise morning note covering overnight developments, earnings reactions, and trade ideas across the coverage universe.
