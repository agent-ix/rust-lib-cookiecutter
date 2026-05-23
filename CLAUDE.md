# rust-lib-cookiecutter

Cookiecutter template generating agent-ix Rust library repos.

## Commands

```bash
cookiecutter . --no-input project_name="Test Crate"   # smoke test
```

Generated repos have their own CLAUDE.md with type-specific commands.

## Source-of-safety

Safety scaffolding is backported from `agent-ix/ecaz` (the org's reference Rust repo).
When ecaz updates its `clippy.toml` / `deny.toml` / `check_unsafe_comments.sh`, mirror the
non-pgrx-specific changes back into this template's `{{ cookiecutter.project_slug }}/` tree.
