"""
Parallel replacement of strings in a file
"""

from lib.file import read_from_file, write_to_file
from lib.pairs import replace_pairs


async def replacer(filename, pairs):
    """Replace strings in a file."""

    string = read_from_file(filename)
    string, replace_count = replace_pairs(string, pairs)
    write_to_file(filename, string)

    return replace_count
