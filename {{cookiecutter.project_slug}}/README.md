# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Installation

Using uv (recommended):

```bash
uv pip install -e .
```

Or using pip:

```bash
pip install -e .
```

## Development

Install development dependencies:

```bash
uv pip install -e ".[dev]"
```

{% if cookiecutter.use_pre_commit == "y" %}Set up pre-commit hooks:

```bash
pre-commit install
```
{% endif %}

## Usage

```python
from {{ cookiecutter.project_slug }} import main

main()
```

## Testing

Run tests with pytest:

```bash
pytest
```

## Code Quality

Format and lint code:

```bash
ruff format .
ruff check .
```

{% if cookiecutter.use_mypy == "y" %}Type checking:

```bash
mypy .
```
{% endif %}

{% if cookiecutter.use_pre_commit == "y" %}Run all checks with pre-commit:

```bash
pre-commit run --all-files
```
{% endif %}

## License

This project is licensed under the {{ cookiecutter.license }} License.
