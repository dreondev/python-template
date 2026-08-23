import pytest

from {{ package_name }}.greeting import greet


def test_greet_returns_greeting_with_name() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_raises_for_empty_name() -> None:
    with pytest.raises(ValueError):
        greet("")
