#!/usr/bin/env python3
"""Validate the generated Codex financial-services adapter."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "codex-financial-services"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def check_manifest() -> None:
    manifest = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
    if manifest.get("name") != "codex-financial-services":
        fail("plugin manifest name must be codex-financial-services")
    for key in ("skills", "mcpServers"):
        rel = manifest.get(key)
        if not isinstance(rel, str):
            fail(f"plugin manifest missing {key}")
        if not (PLUGIN / rel).resolve().exists():
            fail(f"plugin manifest {key} target does not exist: {rel}")

    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    plugins = marketplace.get("plugins", [])
    if not any(p.get("name") == "codex-financial-services" for p in plugins):
        fail("marketplace does not include codex-financial-services")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def check_skills() -> None:
    skills_root = PLUGIN / "skills"
    if not skills_root.exists():
        fail("missing active skills directory")
    skill_files = sorted(skills_root.glob("*/SKILL.md"))
    if [p.parent.name for p in skill_files] != ["codex-financial-services"]:
        fail("active skills directory must contain only the codex-financial-services router")

    names: set[str] = set()
    for path in skill_files:
        fm = frontmatter(path.read_text(encoding="utf-8"))
        name = fm.get("name")
        description = fm.get("description")
        if not name:
            fail(f"{path.relative_to(ROOT)} missing frontmatter name")
        if not description:
            fail(f"{path.relative_to(ROOT)} missing frontmatter description")
        if name in names:
            fail(f"duplicate active skill name: {name}")
        names.add(name)

    resources_root = PLUGIN / "resources" / "skills"
    resource_files = sorted(resources_root.glob("*/SKILL.md"))
    if len(resource_files) < 100:
        fail(f"expected generated resource skills under resources/skills, found {len(resource_files)}")

    resource_names: set[str] = set()
    for path in resource_files:
        fm = frontmatter(path.read_text(encoding="utf-8"))
        name = fm.get("name")
        description = fm.get("description")
        if not name:
            fail(f"{path.relative_to(ROOT)} missing frontmatter name")
        if not description:
            fail(f"{path.relative_to(ROOT)} missing frontmatter description")
        if name in resource_names:
            fail(f"duplicate generated resource skill name: {name}")
        resource_names.add(name)

    print(f"Validated {len(skill_files)} active skill and {len(resource_files)} generated resource skills")


def check_mcp() -> None:
    mcp = load_json(PLUGIN / ".mcp.json")
    if "mcpServers" not in mcp:
        fail(".mcp.json missing mcpServers")
    if not isinstance(mcp["mcpServers"], dict):
        fail(".mcp.json mcpServers must be an object")


def main() -> None:
    check_manifest()
    check_skills()
    check_mcp()
    print("Codex adapter validation passed")


if __name__ == "__main__":
    main()
