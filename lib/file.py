"""File read/write utils."""


def read_from_file(file_name):
    """Read local file content."""
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()


def write_to_file(file_name, content):
    """Write content to local file."""
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)
