[github]:           https://github.com/Saltssaumure/ClassUpdate
[issues]:           https://github.com/Saltssaumure/ClassUpdate/issues
[pullrequest]:      https://github.com/Saltssaumure/ClassUpdate/pulls
[license]:          https://github.com/Saltssaumure/ClassUpdate/blob/main/LICENSE

[discord]:          https://discord.gg/uy8nKQVatp


# ClassUpdate

Update class names of all themes in a folder.

Updating only a single file? Use SyndiShanX's online tool instead: https://syndishanx.github.io/Website/Update_Classes.html


## Credits
- [classchanges](https://github.com/itmesarah/classchanges) by ItsMeSarah for tracking class changes.
- [discordscripts](https://github.com/NyxIsBad/discordscripts) by NyxIsBad (aka. nightflower) for the formatted changes list.
- and especially [Update-Classes](https://github.com/SyndiShanX/Update-Classes) by SyndiShanX for the inspiration.


## Setup and usage
### Requirements
- [git](https://git-scm.com/downloads)
- [Python 3 (3.11 tested)](https://www.python.org/downloads/)

### Usage
⚠ Make a backup of your themes before using this script.

1. Open terminal in your client mod's directory
1. Download this tool
    - `git clone https://github.com/Saltssaumure/ClassUpdate`
2. Edit config.ini if desired
    - See section below for detailed info
3. Run the script
    - `python ./ClassUpdate/replace.py`

### Example
Files marked with `↻` will be updated by the script if using the default config.
```
WorseDiscord/
├── themes/
│   ├── CoolTheme.theme.css ↻
│   ├── DarkMode2.theme.css ↻
│   ├── another.theme.css   ↻
│   └── testfolder/
│       ├── test.theme.css  ↻
│       ├── something.css   ↻
│       └── wargh.txt
├── MyCoolWebsite/
│   ├── site.html
│   └── main.css
└── ClassUpdate (this tool)/
    ├── replace.py
    └── README.md
```


## Config
The config for this script is stored in `config.ini` and can be edited with your favourite text editor (eg. Notepad++).

### Variables
#### ThemeDirectory
- The location of the themes directory to update.
- A path relative to the `ClassUpdate` directory.
- Default: `themes`
#### FileExtension
- The file extension of the files to update.
- Default: `css`
#### UseLocalDiff
- Whether or not to use a local (instead of online) changes file.
- Use `yes` or `no`.
- Default: `no`
#### DiffLocation
- The location of the changes file.
  - If using local diff, a path relative to the `replace.py` file.
  - If using online diff, a full URL.
- Default: `https://raw.githubusercontent.com/SyndiShanX/Update-Classes/main/Changes.txt`

### Creating a new profile
The `config.ini` has two profiles provided, `DEFAULT` and `local`. You can also create new profiles to store various configs.

1. Add a section to `config.ini` starting with the name of the profile in square brackets:
   ```ini
   [UpdateScss]
   ```
2. Underneath, copy and edit variables you wish to change from the `DEFAULT` profile. Any missing variables will inherit its value from `DEFAULT` automatically. This example profile will update `scss` files in `MyThemes` directory using the online changes file at `https://raw.githubusercontent.com/SyndiShanX/Update-Classes/main/Changes.txt`:
   ```ini
   [UpdateScss]
   ThemeDirectory: MyThemes
   FileExtension: scss
   ```
3. Save your changes before running `replace.py`. Enter your profile name when prompted, without square brackets.


## License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU General Public License][license] for more details.

- <span title="Too long; didn't read; not a lawyer">TL;DR;NAL</span>: Do whatever you want with this, as long as you allow others to do the same.


## Questions or suggestions?
- Post [an issue][issues].
- Make [a pull request][pullrequest] if you're extra cool.
- Post on [my support server][discord].