---
name: "command-financial-analysis-ppt-template"
description: "Codex adapter for Claude slash command /ppt-template from financial-analysis. Use when the user types /ppt-template or asks to create a reusable PPT template skill from a PowerPoint template file"
---

## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.

# /ppt-template Command Adapter

Source: `plugins/vertical-plugins/financial-analysis/commands/ppt-template.md`

When this skill triggers, execute the workflow below in Codex. Ask only for missing business inputs that cannot be inferred from the user's prompt or available files.

# PPT Template Creator Command

Create a self-contained PPT template skill from a user-provided PowerPoint template.

## Instructions

1. **Ask for the template file** if not provided:
   - "Please provide the path to your PowerPoint template file (.pptx or .potx)"
   - The template should contain the slide layouts and branding you want to use

2. **Load the ppt-template-creator skill**:
   - Use the `skill: "ppt-template-creator"` tool to load the full skill instructions
   - Follow the workflow in the skill to analyze the template and generate a new skill

3. **Gather additional info**:
   - Company/template name (for naming the skill)
   - Primary use cases (pitch decks, board materials, client presentations, etc.)

4. **Execute the skill workflow**:
   - Analyze template structure (layouts, placeholders, dimensions)
   - Generate skill directory with assets/ and SKILL.md
   - Create example presentation to validate
   - Package the skill

5. **Deliver the packaged skill** to the user
