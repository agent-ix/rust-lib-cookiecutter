# rust-lib-cookiecutter

[![Discord](https://img.shields.io/badge/Discord-Join%20us-5865F2?logo=discord&logoColor=white)](https://discord.gg/k8DVhuYBR2)

Cookiecutter template generating agent-ix Rust library repos.

Generated repos ship with the safety scaffolding backported from `agent-ix/ecaz`:

- `clippy.toml` — MSRV pin + complexity thresholds
- `rustfmt.toml` — 100-char width, `StdExternalCrate` import grouping
- `deny.toml` — allowed-license policy, advisory + source bans
- `rust-toolchain.toml` — explicit stable pin
- `scripts/check_unsafe_comments.sh` — enforces `// SAFETY:` comments on every `unsafe {`
- `.github/workflows/ci.yml` — fmt-check, clippy `-D warnings`, test, license check, unsafe audit

## Use

```bash
cookiecutter https://github.com/agent-ix/rust-lib-cookiecutter.git
```

Or non-interactive:

```bash
cookiecutter https://github.com/agent-ix/rust-lib-cookiecutter.git --no-input \
  org="agent-ix" \
  project_name="My Crate" \
  description="What it does" \
  author="Your Name" \
  email="you@example.com"
```

## Variables

| Variable | Default | Notes |
|---|---|---|
| `org` | `agent-ix` | GitHub org for the generated repo |
| `project_name` | `My Rust Library` | Human-readable name |
| `project_slug` | derived | `lower(project_name).replace(' ', '-')` — dir name + Cargo crate name |
| `project_snake` | derived | `project_slug.replace('-', '_')` — Rust module identifier |
| `description` | `A Rust library.` | One-line crate description |
| `author` | `Your Name` | Cargo `authors` field |
| `email` | `you@example.com` | Cargo `authors` field |
| `rust_msrv` | `1.75` | Clippy `msrv` setting |
| `rust_edition` | `2021` | Cargo edition |
| `version` | `0.1.0` | Initial crate version |
| `license` | `MIT` | SPDX license id; only `MIT` ships a templated LICENSE file |

The template source is MIT licensed. Its default generated project is also MIT
licensed. The `dev-tools` `/new-project` workflow applies its own AGPL policy
to generated projects before their first commit; users invoking Cookiecutter
directly choose their own project license.

## What's NOT in v1

The following ECAZ patterns were considered and intentionally left out of the base template:

- `hardening/` (kani / loom / shuttle / sim-spire) — too project-specific, opt-in via a future variable
- pgrx multi-version test lanes — ecaz-specific (PostgreSQL extension)
- mutation testing, coverage delta gates, flake-hunt, miri-on-main — heavy CI lanes, add per-project when justified
- big-endian qemu / SIMD differential tests — ultra-specialized
- benchmark regression auto-push — bench dir is included, but CI doesn't gate on it
