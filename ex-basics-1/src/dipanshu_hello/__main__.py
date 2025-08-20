"""Console entry for dipanshu_hello"""

import argparse
import sys
from .hello import say_hello


def main() -> None:
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(
        description="Say hello to someone.",
        prog="dipanshu-hello"
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="world",
        help="Name to greet (default: world)"
    )

    try:
        args = parser.parse_args()
        say_hello(args.name)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nGoodbye!", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
