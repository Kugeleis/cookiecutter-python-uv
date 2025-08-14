"""Tests for {{ project_name }}."""

import pytest
from {{ project_slug }}.main import main


def test_main(capsys: pytest.CaptureFixture) -> None:
    """Test the main function."""
    main()
    captured = capsys.readouterr()
    assert "Hello from {{ project_name }}!" in captured.out
