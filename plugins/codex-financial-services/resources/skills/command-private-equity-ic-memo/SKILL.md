---
name: "command-private-equity-ic-memo"
description: "Codex adapter for Claude slash command /ic-memo from private-equity. Use when the user types /ic-memo or asks to draft an investment committee memo"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /ic-memo Command Adapter

Source: `plugins/vertical-plugins/private-equity/commands/ic-memo.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `ic-memo` skill and draft a structured IC memo synthesizing due diligence findings, financial analysis, and deal terms.

If a company name is provided, use it. Otherwise ask the user for the target and available materials.
