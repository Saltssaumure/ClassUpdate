# ClassUpdate

Update class names of all themes in a folder.

Thanks to SyndiShanX for the diff. If you are updating only a single file, use their online tool instead: https://syndishanx.github.io/Website/Update_Classes.html

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