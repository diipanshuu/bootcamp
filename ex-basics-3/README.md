# Greet CLI
## Live demo (asciinema)
Watch the CLI demo:
- [Asciinema link](https://asciinema.org/a/4UZgeJ50Y0eAad7d5q4Pb0pgW)

<a href="https://asciinema.org/a/4UZgeJ50Y0eAad7d5q4Pb0pgW" target="_blank"><img src="https://asciinema.org/a/4UZgeJ50Y0eAad7d5q4Pb0pgW.svg" /></a>

A modern, professional greeting CLI application that says hello to users with beautiful rich colored output, powered by Typer.

## Installation

### For End Users (from TestPyPI)
```bash
# Install from TestPyPI (testing repository)
pip install -i https://test.pypi.org/simple/ dipanshu-hello==0.1.2

# Or install latest version from TestPyPI
pip install -i https://test.pypi.org/simple/ dipanshu-hello
```

## Usage

### As a CLI tool

```bash
# Greet the world (using the main command)
greet-cli

# Greet someone specific
greet-cli "Alice"

# Alternative shorter command
greet "Bob"
```

### As a Python module

```bash
# Run directly
python -m dipanshu_hello

# With a name
python -m dipanshu_hello "Charlie"
```

### As a Python library

```python
from dipanshu_hello import say_hello

# Print and return greeting
message = say_hello("Charlie")
print(f"Returned: {message}")
```

## Features

- **Modern CLI with Typer** - Beautiful, automatically generated help text and command-line interface
- **Rich colored output** - Beautiful green, bold text formatting when Rich library is available
- **Type-safe arguments** - Full type checking and validation for command-line arguments
- **Automatic help generation** - Professional-looking `--help` with formatted sections
- **Graceful fallback** - Works perfectly even without Rich library installed
- Proper error handling for empty names
- Type-annotated codebase
- Comprehensive docstrings
- Cross-platform compatibility

## CLI Usage Examples

```bash
# See all available options and help
greet-cli --help

# Greet the world (default)
greet-cli

# Greet someone specific
greet-cli "Alice"
greet-cli Bob

# Use the shorter alias
greet "Professional User"
```

## Development

This project uses:
- Python 3.8+
- **Typer** for modern CLI framework
- **Rich** for beautiful terminal output
- UV for dependency management
- Type annotations throughout

## License

MIT License
