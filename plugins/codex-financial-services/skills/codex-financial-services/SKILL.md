---
name: "codex-financial-services"
description: "Use this when the user explicitly asks for the codex-financial-services adapter, Anthropic financial-services repo workflows, DCF, comps, LBO, 3-statement models, investment banking pitch workflows, equity research reports, private equity IC memos, fund-admin workflows, KYC screening, GL reconciliation, or Claude/Cowork financial-services style commands such as /dcf, /comps, /earnings, /ic-memo, /lbo, or /model-update. Do not use for broad personal investment advice or vague investment help unless the user asks for one of these workflows."
---

# Codex Financial Services

This is the active router for the generated Codex adapter. Keep the first response fast and bounded.

## First Response Rule

Before reading any large generated workflow file or starting analysis, identify the exact workflow and required input. If the user has not provided a company/ticker, source files, and requested artifact, ask a concise clarification question instead of planning a full model.

Do not silently start a DCF, comps, pitch, or research workflow from a vague prompt. Do not read `resources/skills/dcf-model/SKILL.md`, `resources/skills/comps-analysis/SKILL.md`, or other large files until the user has provided the target company/ticker and confirmed the artifact they want.

For general investment questions, explain that this adapter is for analyst workflows and ask whether they want a DCF, comps, research note, IC memo, or portfolio review. Do not provide personal financial advice.

Generated workflow resources live under:

`resources/skills`

Prefer command adapters for first-pass workflow routing because they are shorter:

- DCF: start with `resources/skills/command-financial-analysis-dcf/SKILL.md`; read `resources/skills/dcf-model/SKILL.md` only after inputs are known.
- Comps: start with `resources/skills/command-financial-analysis-comps/SKILL.md`; read `resources/skills/comps-analysis/SKILL.md` only after peer-set/data needs are known.
- LBO: `resources/skills/command-financial-analysis-lbo/SKILL.md`
- 3-statement model: `resources/skills/command-financial-analysis-3-statement-model/SKILL.md`
- Pitch agent: `resources/skills/agent-pitch-agent/SKILL.md`
- Earnings: `resources/skills/command-equity-research-earnings/SKILL.md`
- IC memo: `resources/skills/command-private-equity-ic-memo/SKILL.md`
- GL reconciliation: `resources/skills/agent-gl-reconciler/SKILL.md`
- KYC: `resources/skills/agent-kyc-screener/SKILL.md`

Treat commercial MCP connectors as optional. If a provider is unavailable, ask for user-provided files or use public sources where suitable.
