---
name: "command-private-equity-source"
description: "Codex adapter for Claude slash command /source from private-equity. Use when the user types /source or asks to source deals — discover companies and draft founder outreach"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /source Command Adapter

Source: `plugins/vertical-plugins/private-equity/commands/source.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `deal-sourcing` skill and run the sourcing pipeline: discover target companies, check CRM for existing relationships, and draft personalized founder outreach emails.

If criteria are provided, use them. Otherwise ask the user for sector, size, geography, and deal parameters.
