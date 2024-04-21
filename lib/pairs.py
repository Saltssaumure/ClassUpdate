"""
Functions for getting and replacing pairs.
"""

import urllib.request

from lib.file import read_from_file


def get_pairs(local_bool, location):
    """Returns list of pairs from local or online diff file."""
    if local_bool is True:
        diff = read_from_file(location).splitlines()
    else:
        with urllib.request.urlopen(location) as response:
            diff = response.read().decode("utf-8").splitlines()

    pairs = [[old_class, new_class]
             for old_class, new_class in zip(diff[::2], diff[1::2])]

    return pairs


def replace_pairs(string, pairs):
    """Replace old content with new content in string."""
    replaces = 0

    for old, new in pairs:
        old_string = string

        pair = f":is(.{old}, .{new})"
        string = string.replace(pair, f".{old}").replace(old, new)

        if old_string != string:
            replaces += 1

    return string, replaces
