---
name: "command-investment-banking-cim"
description: "Codex adapter for Claude slash command /cim from investment-banking. Use when the user types /cim or asks to draft a Confidential Information Memorandum"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /cim Command Adapter

Source: `plugins/vertical-plugins/investment-banking/commands/cim.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `cim-builder` skill and structure a CIM for the specified company.

If a company name is provided, use it. Otherwise ask the user for the target company and available source materials.
