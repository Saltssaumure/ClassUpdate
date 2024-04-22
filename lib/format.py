"""
String formatting utils.
"""


def q(string):
    """Adds quotes around string."""
    return f'"{string}"'


def ind(string, spaces=2):
    """Adds indentation to string."""
    return f"{' ' * spaces}{string}"
