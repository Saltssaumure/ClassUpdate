"""
Get parameters from user input.
"""

import configparser
import glob
import os.path

from lib.format import ind, q

__all__ = ["get_params"]


def try_user(config, profile):
    """Recursively receives user input until valid profile name entered."""
    try:
        config[profile]  # pylint: disable=pointless-statement
        return profile
    except KeyError:
        profile = input(f"{q(profile)} not found:\t\t")
        return try_user(config, profile)


def get_config(config_filename):
    """Get parameters from config file."""
    raw_config = configparser.ConfigParser()
    if not os.path.exists(config_filename):
        raise FileNotFoundError("Config file not found.")
    raw_config.read(config_filename)

    profile = "DEFAULT"
    if input(f"Use {q(profile)} profile? [Y/n]\t").lower() == "n":
        profile = input("Config profile name:\t\t")
        profile = try_user(raw_config, profile)

    config_user = raw_config[profile]
    config = {
        "dir": config_user["ThemeDirectory"],
        "ext": config_user["FileExtension"],
        "uselocaldiff": config_user.getboolean("UseLocalDiff"),
        "location": config_user["DiffLocation"],
    }

    return config


def get_params():
    """Return parameters."""
    config = get_config("config.ini")
    print(ind(f"Themes directory:\t{config['dir']}"))
    print(ind(f"File extension:\t{config['ext']}"))
    print(ind(f"Use local diff:\t{config['uselocaldiff']}"))
    print(ind(f"Diff file location:\t{config['location']}"))

    filenames = glob.glob(os.path.join(
        "..", config["dir"], "**", "*." + config["ext"]
    ), recursive=True)

    print(f"\nFound {len(filenames)} {config['ext']} files in {config['dir']}.")
    input("Press enter to continue or Ctrl+C to cancel.")

    return config["uselocaldiff"], config['location'], filenames
