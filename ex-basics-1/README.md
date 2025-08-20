# Greeting CLI Tool

A simple CLI application that greets users with a friendly hello message.

## Installation

### For End Users (from TestPyPI)
```bash
# Install from TestPyPI (testing repository)
pip install -i https://test.pypi.org/simple/ dipanshu-hello==0.1.0

# Or install latest version from TestPyPI
pip install -i https://test.pypi.org/simple/ dipanshu-hello
```

## Usage

### As a CLI tool

```bash
# Greet the world
dipanshu-hello

# Greet someone specific
dipanshu-hello "Alice"
```

### As a Python module

```bash
# Run directly
python -m dipanshu_hello

# With a name
python -m dipanshu_hello "Bob"
```

### As a Python library

```python
from dipanshu_hello import say_hello

# Print and return greeting
message = say_hello("Charlie")
print(f"Returned: {message}")
```

## Features

- Simple and clean CLI interface
- Proper error handling for empty names
- Type-annotated codebase
- Comprehensive docstrings
- Cross-platform compatibility

## Development

This project uses:
- Python 3.13+
- UV for dependency management
- Type annotations throughout

## License

MIT License
