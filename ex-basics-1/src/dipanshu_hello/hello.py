"""dipanshu_hello.hello - core greeting functionality"""


def say_hello(name: str = "world") -> str:
    """
    Print and return a greeting message.

    Args:
        name: Name to greet. Defaults to "world" if empty or whitespace.

    Returns:
        The greeting message.
    """
    # If name is empty or only whitespace, use default "world"
    if not name or not name.strip():
        name = "world"
    else:
        name = name.strip()

    msg = f"Hello, {name}!"
    print(msg)
    return msg
