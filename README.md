# ClassUpdate

Update class names of all themes in a folder.

Updating only a single file? Use SyndiShanX's online tool instead: https://syndishanx.github.io/Website/Update_Classes.html

## Credits
- [classchanges](https://github.com/itmesarah/classchanges) by ItsMeSarah for tracking class changes.
- [discordscripts](https://github.com/NyxIsBad/discordscripts) by NyxIsBad (aka. nightflower) for the formatted changes list.
- and especially [Update-Classes](https://github.com/SyndiShanX/Update-Classes) by SyndiShanX for the inspiration.

## Requirements
- [git](https://git-scm.com/downloads)
- [Python 3 (3.11 tested)](https://www.python.org/downloads/)

## Usage
⚠ Make a backup of your themes before using this script.

Next to themes folder:
1. `git clone https://github.com/Saltssaumure/ClassUpdate`
2. `cd ./ClassUpdate`
3. `python ./replace.py`

Feel free to delete or move the `ClassUpdate` folder after use.

## Default values
| Variable         | Default value                                                                  |
| ---------------- | ------------------------------------------------------------------------------ |
| Themes directory | `themes`                                                                       |
| File extension   | `css`                                                                          |
| Diff URL         | `https://raw.githubusercontent.com/SyndiShanX/Update-Classes/main/Changes.txt` |

## Example
Files marked with `↻` will be updated by the script if using the default values above.
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