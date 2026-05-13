---
name: "command-private-equity-dd-prep"
description: "Codex adapter for Claude slash command /dd-prep from private-equity. Use when the user types /dd-prep or asks to prep for a diligence meeting or expert call"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /dd-prep Command Adapter

Source: `plugins/vertical-plugins/private-equity/commands/dd-prep.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `dd-meeting-prep` skill and generate targeted questions, benchmarks, and red flags to probe.

If details are provided, use them. Otherwise ask for the company, meeting type (management presentation, expert call, customer reference), and topic focus.
