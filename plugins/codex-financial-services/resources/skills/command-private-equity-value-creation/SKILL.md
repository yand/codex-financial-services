---
name: "command-private-equity-value-creation"
description: "Codex adapter for Claude slash command /value-creation from private-equity. Use when the user types /value-creation or asks to build a post-acquisition value creation plan"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /value-creation Command Adapter

Source: `plugins/vertical-plugins/private-equity/commands/value-creation.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `value-creation-plan` skill and structure a value creation roadmap with EBITDA bridge, 100-day plan, and KPI dashboard.

If a company name is provided, use it. Otherwise ask the user for the target company details.
