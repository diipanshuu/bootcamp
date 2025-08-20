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

from .constants import DEFAULT_GREETING_STYLE, DEFAULT_NAME, GREETING_TEMPLATE


def _create_console() -> Optional[Console]:
    """
    Create a Rich console instance if available.

    Returns:
        Console instance if Rich is available, None otherwise.
    """
    if RICH_AVAILABLE and Console:
        return Console()
    return None


def _print_with_rich(console: Console, message: str) -> None:
    """
    Print message using Rich console with formatting.

    Args:
        console: Rich Console instance.
        message: Message to print with rich formatting.
    """
    if console and Text:
        formatted_text = Text(message, style=DEFAULT_GREETING_STYLE)
        console.print(formatted_text)


def _print_fallback(message: str) -> None:
    """
    Print message using standard print as fallback.

    Args:
        message: Message to print using standard output.
    """
    print(message)


def _validate_and_clean_name(name: Optional[str]) -> str:
    """
    Validate and clean the input name.

    Args:
        name: Input name to validate and clean.

    Returns:
        Cleaned name string.
    """
    if not name or not name.strip():
        return DEFAULT_NAME
    return name.strip()


def _create_greeting_message(name: str) -> str:
    """
    Create a greeting message for the given name.

    Args:
        name: Name to include in greeting.

    Returns:
        Formatted greeting message.
    """
    return GREETING_TEMPLATE.format(name=name)


def say_hello(name: Optional[str] = None) -> str:
    """
    Print and return a greeting message with rich formatting if available.

    Args:
        name: Name to greet. Defaults to DEFAULT_NAME if empty or None.

    Returns:
        The greeting message string.
    """
    cleaned_name = _validate_and_clean_name(name)
    message = _create_greeting_message(cleaned_name)
    console = _create_console()

    if console:
        _print_with_rich(console, message)
    else:
        _print_fallback(message)

    return message
