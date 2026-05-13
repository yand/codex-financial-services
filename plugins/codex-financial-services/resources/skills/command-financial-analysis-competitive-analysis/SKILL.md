---
name: "command-financial-analysis-competitive-analysis"
description: "Codex adapter for Claude slash command /competitive-analysis from financial-analysis. Use when the user types /competitive-analysis or asks to create a competitive landscape analysis"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /competitive-analysis Command Adapter

Source: `plugins/vertical-plugins/financial-analysis/commands/competitive-analysis.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

Load the `competitive-analysis` skill and build a competitive landscape analysis for the specified company or industry.

If a company/industry is provided as an argument, use it. Otherwise ask the user what they want to analyze.
