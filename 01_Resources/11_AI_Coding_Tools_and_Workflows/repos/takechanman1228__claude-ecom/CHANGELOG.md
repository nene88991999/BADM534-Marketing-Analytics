# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.2.0] — 2026-06-11

Plugin-first distribution and skill refactor.

### Changed
- The Claude Code plugin is now the primary install path
  (`/plugin marketplace add takechanman1228/claude-ecom` then
  `/plugin install claude-ecom@claude-ecom`)
- New self-bootstrapping launcher `bin/ecom` (on PATH while the plugin is
  enabled): installs the Python backend into a persistent venv at
  `~/.local/share/claude-ecom/` that survives plugin updates, and
  reinstalls automatically when the plugin version changes (fixes stale
  venvs after updates)
- SKILL.md slimmed from 564 to ~190 lines per current skill guidelines
  (<500 lines); details split into three new on-demand references:
  `review-schema.md`, `report-format.md`, `focused-query.md`
- Skill frontmatter modernized: trigger phrases moved to `when_to_use`,
  `allowed-tools` narrowed to `Bash(ecom *)`, stale `version` field
  dropped (plugin.json is the single version source)
- Dollar amounts followed by digits removed from SKILL.md body (they
  collide with positional-argument substitution in current Claude Code)
- CI validates the plugin with `claude plugin validate --strict`
  (replaces validate-skills.sh)

### Removed
- Legacy curl installer: `install.sh`, `install.ps1`, `uninstall.sh`,
  `uninstall.ps1` — see the README migration note for removing
  `~/.claude/skills/ecom`
- `validate-skills.sh` and `scripts/setup.sh`

## [0.1.0] — 2026-03-06

Initial release.

- Single `ecom review` command for full-store health review
- Multi-period architecture: 30d / 90d / 365d trailing windows with automatic data coverage detection
- ~30 health checks across Revenue (40%), Customer (30%), Product (30%)
- Each check returns pass / watch / fail
- KPI tree with growth drivers (AOV / volume / mix effects)
- review.json output with top issues and action candidates
- Claude Code skill (`/ecom review`) with full review and focused query modes
- Shopify CSV and generic CSV format support with fuzzy column mapping
- Install script for bash and PowerShell
