"""Console entry for dipanshu_hello with Typer CLI framework"""

import typer
from typing_extensions import Annotated
from .hello import say_hello
from .constants import (
    CLI_NAME,
    CLI_HELP_MESSAGE,
    GOODBYE_MESSAGE,
    NAME_HELP_TEXT,
    MAIN_DOCSTRING,
    DEFAULT_NAME
)


# Create the Typer app instance
app = typer.Typer(
    name=CLI_NAME,
    help=CLI_HELP_MESSAGE,
    add_completion=False
)


def _handle_keyboard_interrupt() -> None:
    """Handle keyboard interrupt gracefully."""
    typer.echo(GOODBYE_MESSAGE, err=True)
    raise typer.Exit(0)


def _handle_import_error(exc: ImportError) -> None:
    """Handle missing dependency errors."""
    typer.echo(f"Missing dependency: {exc}", err=True)
    typer.echo("Please install with: pip install dipanshu-hello", err=True)
    raise typer.Exit(1)


def _handle_value_error(exc: ValueError) -> None:
    """Handle input validation errors."""
    typer.echo(f"Invalid input: {exc}", err=True)
    raise typer.Exit(1)


def _execute_greeting(name: str) -> None:
    """
    Execute the greeting with proper error handling.

    Args:
        name: Name to greet.
    """
    try:
        say_hello(name)
    except KeyboardInterrupt:
        _handle_keyboard_interrupt()
    except ImportError as exc:
        _handle_import_error(exc)
    except ValueError as exc:
        _handle_value_error(exc)
    except (OSError, RuntimeError) as exc:
        typer.echo(f"System error: {exc}", err=True)
        raise typer.Exit(1)


def main_command(
    name: Annotated[str, typer.Argument(help=NAME_HELP_TEXT)] = DEFAULT_NAME
) -> None:
    """
    Say hello to someone with beautiful colored output.

    Args:
        name: Name to greet. Defaults to DEFAULT_NAME if not provided.
    """
    _execute_greeting(name)


# Register the main function as the default command
app.command()(main_command)


def main() -> None:
    """Entry point for console scripts."""
    app()


if __name__ == "__main__":
    app()
