---
name: "command-private-equity-ai-readiness"
description: "Codex adapter for Claude slash command /ai-readiness from private-equity. Use when the user types /ai-readiness or asks to scan the portfolio for the highest-leverage AI opportunities"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /ai-readiness Command Adapter

Source: `plugins/vertical-plugins/private-equity/commands/ai-readiness.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `ai-readiness` skill and scan portfolio companies for AI leverage — per-company go / no-go gate, quick wins ranked by EBITDA impact across the portfolio, and replays that hit multiple companies at once.

If a folder or company list is provided, use it. Otherwise ask which companies to include and for their latest quarterly materials.
