# ClassUpdate

Update classes of Discord themes automagically. The diff file is adapted from 11pixels' provided diff files.

## Usage
⚠ Make a backup of your theme before using this script.

In your theme's root directory:
1. `git clone https://github.com/Saltssaumure/ClassUpdate`
2. `cd ./ClassUpdate`
3. `python ./replace.py`

Delete or move the `ClassUpdate` folder after use.

### Default values
| Variable             | Default value |
| -------------------- | ------------- |
| S/CSS directory      | `scss`        |
| S/CSS file extension | `*.scss`      |
| Diff file name       | `diff.diff`   |

### Assumed file structure
Files marked with `↻` will be updated by the script if using the default values above.
```
MyTheme
├── scss
│   ├── main.scss ↻
│   ├── main.css
│   └── components
│       ├── _stuff.scss ↻
│       └── _things.scss ↻
├── otherstuff
│   └── test.scss
└── ClassUpdate (this tool)
    ├── diff.diff
    ├── replace.py
    └── README.md
```
