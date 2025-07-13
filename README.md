# Cookiecutter Python UV Template

A modern Python project template using [uv](https://github.com/astral-sh/uv) for fast dependency management.

## Features

- **Modern packaging** with `pyproject.toml` and `src/` layout
- **Fast dependencies** with `uv` package manager
- **Code quality** with `ruff` (linting + formatting)
- **Type checking** with `mypy` (optional)
- **Testing** with `pytest` + coverage (optional)
- **Pre-commit hooks** for automated code quality (optional)

## Usage

Install cookiecutter:

```bash
pip install cookiecutter
```

Generate a new project:

```bash
cookiecutter https://github.com/yourusername/cookiecutter-python-uv
```

Or use this local template:

```bash
cookiecutter .
```

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- cookiecutter

## Generated Project Structure

```
my_project/
├── src/my_project/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── pyproject.toml
├── README.md
└── .pre-commit-config.yaml  # if enabled
```