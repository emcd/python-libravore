# Project Guidance

Project-owned knowledge the generated `AGENTS.md` entrypoint must not own.
Structured tracking stays in `nb`.

## Purpose

PyPI misspelling-redirect and name-reservation package for
[`librovore`](https://pypi.org/project/librovore/) (`emcd/python-librovore`):

- Emits a `UserWarning` on import to alert users that `libravore` is a common
  misspelling of `librovore`.
- Re-exports `librovore` (`from librovore import *` in
  `sources/libravore/__init__.py`) so accidental installs or imports continue to
  work while directing users to the intended package.
- Reserves the `libravore` distribution name on PyPI for a potential future
  project ("devourer of [model] weights").

## Tech Stack

- **Language & runtime**: Python `>= 3.10` (CPython 3.10–3.13, PyPy 3.10);
  runtime dependencies `librovore` and `typing-extensions`.
- **Build & environments**: Hatch / Hatchling (`pyproject.toml`, `hatch --env
  develop`).
- **Validation & docs**: Ruff, isort, Pyright, Vulture, pytest + coverage,
  Sphinx (Furo, MyST), Towncrier, pre-commit.
- **Templates**: Managed via Copier from `emcd/python-project-common`
  (`.auxiliary/configuration/copier-answers.yaml`) and `emcd/agents-common`
  (`.auxiliary/configuration/copier-answers--agents.yaml`).

## Notes

- Keep the package minimal while it serves as a redirect placeholder; real
  functionality belongs in `emcd/python-librovore`.
- Durable links:
  - Package overview: `README.rst`
  - Product requirements & architecture: `documentation/prd.rst`,
    `documentation/architecture/`
  - Target package: https://github.com/emcd/python-librovore
    (PyPI: https://pypi.org/project/librovore/)
