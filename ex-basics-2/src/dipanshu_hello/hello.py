# src/dipanshu_hello/hello.py
"""dipanshu_hello.hello - core greeting functionality with rich output"""

from typing import Optional

try:
    from rich.console import Console
    from rich.text import Text
    RICH_AVAILABLE = True
except ImportError:
    # Rich is not available, will use fallback
    RICH_AVAILABLE = False
    Console = None
    Text = None


def _create_console() -> Optional[object]:
    """
    Create a Rich console instance if available.

    Returns:
        Console instance if Rich is available, None otherwise.
    """
    if RICH_AVAILABLE:
        return Console()
    return None


def _print_with_rich(console: object, message: str) -> None:
    """
    Print message using Rich console with formatting.

    Args:
        console: Rich Console instance.
        message: Message to print.
    """
    if console and Text:
        formatted_text = Text(message, style="bold green")
        console.print(formatted_text)


def _print_fallback(message: str) -> None:
    """
    Print message using standard print as fallback.

    Args:
        message: Message to print.
    """
    print(message)


def say_hello(name: str = "world") -> str:
    """
    Print and return a greeting message with rich formatting if available.

    Args:
        name: Name to greet. Defaults to "world" if empty or None.

    Returns:
        The greeting message string.
    """
    # Handle empty or None input
    if not name or not name.strip():
        name = "world"
    else:
        name = name.strip()

    message = f"Hello, {name}!"
    console = _create_console()

    if console:
        _print_with_rich(console, message)
    else:
        _print_fallback(message)

    return message
