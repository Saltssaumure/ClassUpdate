"""
Get parameters from user input.
"""

import glob
import os.path

DEFAULT = {
    "dir": "themes",
    "ext": "css",
    "localdiff": "N",
    "filename": "Changes.txt",
    "url": "https://raw.githubusercontent.com/SyndiShanX/Update-Classes/main/Changes.txt"
}


def get_params_from_user():
    """Get parameters from user input."""

    print("Leave blank to use default values.")
    css_dir = input(f"Themes directory \t(default: {DEFAULT['dir']}):\t") or DEFAULT["dir"]
    css_ext = input(f"File extension \t\t(default: {DEFAULT['ext']}):\t\t") or DEFAULT["ext"]
    local = input(
        f"Use local diff? [y/N]\t(default: {DEFAULT['localdiff']}):\t\t"
    ) or DEFAULT['localdiff']

    if local.lower() == "y":
        local_bool = True
        location = DEFAULT["filename"]
        location = input(
            f"Diff file location\t(default: {DEFAULT['filename']}):\t"
        ) or DEFAULT['filename']
    else:
        local_bool = False
        location = input(f"Diff URL \t\t(default: {DEFAULT['url']}):\t") or DEFAULT['url']

    print("\nUsing values:")
    print(f"Themes directory:\t{css_dir}")
    print(f"File extension:\t\t{css_ext}")
    print(f"Use local diff:\t\t{local_bool}")
    if local_bool is True:
        print(f"Diff file location:\t{location}")
    else:
        print(f"Diff URL:\t\t{location}")

    filenames = glob.glob(os.path.join("..", css_dir, "**", "*." + css_ext), recursive=True)

    print(f"\nFound {len(filenames)} {css_ext} files in {css_dir}.")
    input("Press enter to continue or Ctrl+C to cancel.")

    return local_bool, location, filenames
