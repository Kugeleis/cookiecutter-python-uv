# Python Project Template (Copier & Cookiecutter)

A modern Python project template using [uv](https://github.com/astral-sh/uv) for fast dependency management. Designed for use with [Copier](https://copier.readthedocs.io/) and [Cookiecutter](https://cookiecutter.readthedocs.io/).

## Features

- **Modern packaging** with `pyproject.toml` and `src/` layout
- **Copier & Cookiecutter** support for project generation and updates
- **Fast dependencies** with `uv` package manager
- **Code quality** with `ruff` (linting + formatting) (optional)
- **Type checking** with `mypy` (optional)
- **Testing** with `pytest` + coverage (optional)
- **Pre-commit hooks** for automated code quality (optional)

## Usage

This template can be used with either Copier or Cookiecutter. **Copier is recommended** as it allows you to update your project from the template in the future.

### With Copier (Recommended)

1.  **Install Copier:**
    ```bash
    pip install copier
    ```

2.  **Generate a new project:**
    ```bash
    copier copy gh:yourusername/cookiecutter-python-uv my-new-project
    ```
    *(Replace `yourusername` and `my-new-project`)*

    To use the local template, run `copier copy . my-new-project`.

3.  **Update your project:**
    To update your project to the latest version of the template, navigate to your project's directory and run:
    ```bash
    copier update
    ```

### With Cookiecutter

1.  **Install Cookiecutter:**
    ```bash
    pip install cookiecutter
    ```

2.  **Generate a new project:**
    ```bash
    cookiecutter gh:yourusername/cookiecutter-python-uv
    ```
    *(Replace `yourusername`)*

    To use the local template, run `cookiecutter .`.

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- [Copier](https://copier.readthedocs.io/) or [Cookiecutter](https://cookiecutter.readthedocs.io/)

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