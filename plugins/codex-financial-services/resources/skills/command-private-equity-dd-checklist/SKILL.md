---
name: "command-private-equity-dd-checklist"
description: "Codex adapter for Claude slash command /dd-checklist from private-equity. Use when the user types /dd-checklist or asks to generate a due diligence checklist"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /dd-checklist Command Adapter

Source: `plugins/vertical-plugins/private-equity/commands/dd-checklist.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `dd-checklist` skill and generate a comprehensive, sector-tailored due diligence checklist with status tracking.

If a company name is provided, use it. Otherwise ask the user for the target company and deal details.
