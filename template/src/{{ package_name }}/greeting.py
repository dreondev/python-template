"""Greeting helpers."""


def greet(name: str) -> str:
    """Build a greeting for the given name.

    Args:
        name: Name of the person to greet.

    Returns:
        The formatted greeting.

    Raises:
        ValueError: If name is empty or whitespace only.
    """
    if not name.strip():
        raise ValueError("Name must not be empty")
    return f"Hello, {name}!"
