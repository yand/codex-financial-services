#!/usr/bin/env python3
"""Generate a Codex plugin adapter from the Claude financial-services repo."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "plugins" / "codex-financial-services"
SKILLS_OUT = OUT / "skills"

SOURCE_PLUGIN_ROOTS = [
    ROOT / "plugins" / "vertical-plugins",
    ROOT / "plugins" / "partner-built",
]

AGENT_ROOT = ROOT / "plugins" / "agent-plugins"

PLUGIN_DESCRIPTION = (
    "Codex adapter for Anthropic's Financial Services Claude/Cowork plugin "
    "collection: financial modeling, investment banking, equity research, "
    "private equity, wealth management, fund admin, operations, and partner "
    "financial data workflows."
)

OPTIONAL_CONNECTOR_NOTE = """\
## Codex Adapter Notes

- This skill was adapted from Anthropic's Claude/Cowork financial-services repo.
- Use available Codex tools, local files, web research, spreadsheets, documents, and presentations to perform the workflow.
- Treat referenced commercial MCP providers as optional. If the provider is not configured, ask for user-provided data or use public sources where suitable.
- Claude-specific slash command, agent, hook, and tool names are preserved as source context; map them to equivalent Codex behavior rather than requiring Claude runtime features.
"""


def slug(text: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "item"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        data[key.strip()] = value
    return data, body


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_skill(name: str, description: str, body: str) -> str:
    return (
        "---\n"
        f"name: {yaml_quote(name)}\n"
        f"description: {yaml_quote(description)}\n"
        "---\n\n"
        f"{OPTIONAL_CONNECTOR_NOTE}\n"
        f"{body.lstrip()}"
    )


def copy_skill_dir(src: Path, dest: Path, name: str, description: str) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    ignore = shutil.ignore_patterns(".claude-plugin", "__pycache__", ".DS_Store")
    shutil.copytree(src, dest, ignore=ignore)
    fm, body = split_frontmatter(read_text(src / "SKILL.md"))
    final_name = name or fm.get("name") or src.name
    final_description = description or fm.get("description") or f"Codex adapter skill for {final_name}."
    (dest / "SKILL.md").write_text(
        render_skill(final_name, final_description, body), encoding="utf-8"
    )
    write_openai_yaml(dest, final_name, final_description)


def write_openai_yaml(skill_dir: Path, name: str, description: str) -> None:
    agents_dir = skill_dir / "agents"
    agents_dir.mkdir(exist_ok=True)
    display = name.replace("-", " ").title()
    short = description[:117] + "..." if len(description) > 120 else description
    (agents_dir / "openai.yaml").write_text(
        "\n".join(
            [
                f"display_name: {yaml_quote(display)}",
                f"short_description: {yaml_quote(short)}",
                f"default_prompt: {yaml_quote('Use the ' + name + ' workflow.')}",
                "",
            ]
        ),
        encoding="utf-8",
    )


def source_plugin_dirs() -> list[Path]:
    dirs: list[Path] = []
    for root in SOURCE_PLUGIN_ROOTS:
        if root.exists():
            dirs.extend(sorted(p for p in root.iterdir() if p.is_dir()))
    return dirs


def convert_source_skills() -> list[dict[str, str]]:
    seen_names: set[str] = set()
    converted: list[dict[str, str]] = []
    for plugin_dir in source_plugin_dirs():
        skills_dir = plugin_dir / "skills"
        if not skills_dir.exists():
            continue
        for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
            src_skill = skill_md.parent
            fm, _ = split_frontmatter(read_text(skill_md))
            base_name = slug(fm.get("name") or src_skill.name)
            if base_name == "skill-creator":
                base_name = slug(f"{plugin_dir.name}-{base_name}")
            name = base_name
            if name in seen_names:
                name = slug(f"{plugin_dir.name}-{base_name}")
            seen_names.add(name)
            description = fm.get("description") or f"Codex adapter skill for {name}."
            copy_skill_dir(src_skill, SKILLS_OUT / name, name, description)
            converted.append(
                {
                    "kind": "skill",
                    "name": name,
                    "source": str(src_skill.relative_to(ROOT)),
                }
            )
    return converted


def convert_commands() -> list[dict[str, str]]:
    converted: list[dict[str, str]] = []
    for plugin_dir in source_plugin_dirs():
        commands_dir = plugin_dir / "commands"
        if not commands_dir.exists():
            continue
        for command_file in sorted(commands_dir.glob("*.md")):
            command = command_file.stem
            raw = read_text(command_file)
            fm, body = split_frontmatter(raw)
            name = slug(f"command-{plugin_dir.name}-{command}")
            trigger = f"/{command}"
            description = fm.get("description") or f"Run the {trigger} workflow."
            description = (
                f"Codex adapter for Claude slash command {trigger} from "
                f"{plugin_dir.name}. Use when the user types {trigger} or asks to "
                f"{description[0].lower() + description[1:]}"
            )
            dest = SKILLS_OUT / name
            dest.mkdir(parents=True, exist_ok=True)
            command_body = (
                f"# {trigger} Command Adapter\n\n"
                f"Source: `{command_file.relative_to(ROOT)}`\n\n"
                "When this skill triggers, execute the workflow below in Codex. "
                "Ask only for missing business inputs that cannot be inferred from "
                "the user's prompt or available files.\n\n"
                f"{body.lstrip()}"
            )
            (dest / "SKILL.md").write_text(
                render_skill(name, description, command_body), encoding="utf-8"
            )
            write_openai_yaml(dest, name, description)
            converted.append(
                {
                    "kind": "command",
                    "name": name,
                    "source": str(command_file.relative_to(ROOT)),
                }
            )
    return converted


def convert_agents() -> list[dict[str, str]]:
    converted: list[dict[str, str]] = []
    if not AGENT_ROOT.exists():
        return converted
    for agent_file in sorted(AGENT_ROOT.glob("*/agents/*.md")):
        raw = read_text(agent_file)
        fm, body = split_frontmatter(raw)
        base_name = slug(fm.get("name") or agent_file.stem)
        name = slug(f"agent-{base_name}")
        description = fm.get("description") or f"Codex adapter for {base_name}."
        description = (
            f"Codex adapter for the Claude Cowork {base_name} agent. {description}"
        )
        dest = SKILLS_OUT / name
        dest.mkdir(parents=True, exist_ok=True)
        agent_body = (
            f"# {base_name} Agent Adapter\n\n"
            f"Source: `{agent_file.relative_to(ROOT)}`\n\n"
            "Run this as an orchestrated Codex workflow in the current chat. "
            "Use the generated Codex skills named in the workflow, and do not "
            "assume Claude Cowork agent runtime features are available.\n\n"
            f"{body.lstrip()}"
        )
        (dest / "SKILL.md").write_text(
            render_skill(name, description, agent_body), encoding="utf-8"
        )
        write_openai_yaml(dest, name, description)
        converted.append(
            {"kind": "agent", "name": name, "source": str(agent_file.relative_to(ROOT))}
        )
    return converted


def merge_mcp_configs() -> dict[str, object]:
    servers: dict[str, object] = {}
    for mcp_path in sorted(
        list((ROOT / "plugins").glob("*/*/.mcp.json"))
        + list((ROOT / "claude-for-msft-365-install").glob(".mcp.json"))
    ):
        try:
            data = json.loads(read_text(mcp_path))
        except json.JSONDecodeError:
            continue
        for name, config in data.get("mcpServers", {}).items():
            servers.setdefault(name, config)
    return {"mcpServers": servers}


def write_plugin_manifest() -> None:
    manifest = {
        "name": "codex-financial-services",
        "version": "0.1.0",
        "description": PLUGIN_DESCRIPTION,
        "author": {
            "name": "Codex adapter maintainers",
            "url": "https://github.com/anthropics/financial-services",
        },
        "homepage": "https://github.com/anthropics/financial-services",
        "repository": "https://github.com/anthropics/financial-services",
        "license": "Apache-2.0",
        "keywords": [
            "codex",
            "financial-services",
            "investment-banking",
            "equity-research",
            "private-equity",
            "wealth-management",
            "mcp",
        ],
        "skills": "./skills/",
        "mcpServers": "./.mcp.json",
        "interface": {
            "displayName": "Codex Financial Services",
            "shortDescription": "Financial modeling and markets workflows for Codex",
            "longDescription": PLUGIN_DESCRIPTION,
            "developerName": "Codex adapter maintainers",
            "category": "Productivity",
            "capabilities": ["Interactive", "Write"],
            "websiteURL": "https://github.com/anthropics/financial-services",
            "privacyPolicyURL": "https://www.anthropic.com/legal/privacy",
            "termsOfServiceURL": "https://www.anthropic.com/legal/consumer-terms",
            "defaultPrompt": [
                "Build a DCF model from my financial inputs.",
                "Run comps analysis for this public company.",
                "Draft an investment banking pitch workflow.",
            ],
            "brandColor": "#111827",
        },
    }
    manifest_dir = OUT / ".codex-plugin"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    (manifest_dir / "plugin.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )


def write_marketplace() -> None:
    marketplace = {
        "name": "codex-financial-services",
        "interface": {"displayName": "Codex Financial Services"},
        "plugins": [
            {
                "name": "codex-financial-services",
                "source": {
                    "source": "local",
                    "path": "./plugins/codex-financial-services",
                },
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_USE",
                },
                "category": "Productivity",
            }
        ],
    }
    target = ROOT / ".agents" / "plugins"
    target.mkdir(parents=True, exist_ok=True)
    (target / "marketplace.json").write_text(
        json.dumps(marketplace, indent=2) + "\n", encoding="utf-8"
    )


def write_index(converted: list[dict[str, str]]) -> None:
    lines = [
        "# Codex Financial Services Adapter",
        "",
        "Generated from Anthropic's Claude/Cowork financial-services plugin sources.",
        "",
        "## Contents",
        "",
    ]
    counts: dict[str, int] = {}
    for item in converted:
        counts[item["kind"]] = counts.get(item["kind"], 0) + 1
    for kind in sorted(counts):
        lines.append(f"- {counts[kind]} {kind} adapters")
    lines.extend(["", "## Generated Items", ""])
    for item in converted:
        lines.append(f"- `{item['name']}` ({item['kind']}) from `{item['source']}`")
    lines.append("")
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    SKILLS_OUT.mkdir(parents=True)
    converted: list[dict[str, str]] = []
    converted.extend(convert_source_skills())
    converted.extend(convert_commands())
    converted.extend(convert_agents())
    (OUT / ".mcp.json").write_text(
        json.dumps(merge_mcp_configs(), indent=2) + "\n", encoding="utf-8"
    )
    write_plugin_manifest()
    write_marketplace()
    write_index(converted)
    print(
        f"Generated {len(converted)} Codex adapters in "
        f"{OUT.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
