# python-template

Copier template for Python projects: uv, src layout, ruff, mypy strict,
pytest, pre-commit, commitizen, mkdocs.

## Creating a project

Replace `<project-name>` with your actual project name, for example
`kraken-dca-scheduler`.

```bash
uvx copier copy gh:dreondev/python-template <project-name>
cd <project-name>
uv sync
git init
git branch -m develop
uv run pre-commit install
uv run pre-commit install --hook-type commit-msg
uv run pre-commit install --hook-type pre-push
git add -A
git commit -m "chore: initialize project from template"```

Copier will then ask for the project name, the Python import name and a
short description.

## GitHub setup

After creating the repository on GitHub:

1. Push `develop`, then create `main` from it
2. Settings, General: enable "Automatically delete head branches"
3. Install the `dreondev-release-bot` app on the new repository
   (github.com/settings/apps)
4. Settings, Secrets and variables, Actions:
   - Variable `RELEASE_APP_ID` with the app id
   - Secret `RELEASE_APP_PRIVATE_KEY` with the app private key
5. Settings, Rules, Rulesets, Import a ruleset: upload both files from
   `.github/rulesets/`

Rulesets are only enforced on public repositories under a free personal
account.

## Updating the shared CI

Workflow logic lives in `dreondev/python-ci` and is referenced by tag
`v1`. Changes there apply to all projects once the tag is moved.