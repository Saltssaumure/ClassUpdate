"""
Functions for getting and replacing pairs.
"""

import urllib.request

from lib.file import read_from_file


def get_pairs(local_bool, location):
    """Returns dict of pairs from local or online diff file."""
    if local_bool is True:
        diff = read_from_file(location).splitlines()
    else:
        with urllib.request.urlopen(location) as response:
            diff = response.read().decode("utf-8").splitlines()

    pairs = dict(zip(diff[::2], diff[1::2])).items()

    return pairs


def replace_pairs(string, pairs):
    """Replace old content with new content in string."""
    replaces = 0

    for old, new in pairs:
        old_string = string

        string = string.replace(old, new)

        if old_string != string:
            replaces += 1

    return string, replaces
