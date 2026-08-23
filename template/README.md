# {{ project_name }}

{{ project_description }}

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run pre-commit install
uv run pre-commit install --hook-type commit-msg
uv run pre-commit install --hook-type pre-push
```

Commit the generated `uv.lock` — CI runs `uv sync --locked` and fails
without it.

## Tasks

```bash
uv run poe check      # lint, typecheck, test, audit
uv run poe lint
uv run poe format
uv run poe typecheck
uv run poe test
uv run poe audit
uv run poe hooks      # run all pre-commit hooks
uv run poe docs       # serve docs at localhost:8000
```

## Commits

Conventional Commits are enforced. The version is derived from commit
types on release: `feat` bumps minor, `fix` bumps patch, others do not
bump.

## Notes for Windows

Do not create config files with `echo x > file.toml` in PowerShell — it
writes a BOM that breaks TOML parsers. Use an editor or
`Set-Content -Encoding utf8NoBOM`.

Line endings are normalized to LF via `.gitattributes`.

## Releasing

Merge `develop` into `main` via pull request. The release workflow then
bumps the version, updates the changelog and creates the tag.

When merging, clear the extended description. It repeats the commit
messages, and commitizen would count them twice in the changelog.

## Template updates

This project was generated with copier. To pull in template changes:

```bash
uvx copier update
```

Keep `.copier-answers.yml` in version control — it records which
template version this project came from.
