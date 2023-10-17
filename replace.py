import re, os, glob

cssDir = "scss"
cssExt = "*.scss"
diffFileName = "diff.diff"
useBothClasses = "Y"

# Comment out this section if you want to just hardcode the values.
print("Leave blank to use default values.")
cssDir = input(f"S/CSS directory \t(default: {cssDir}):\t") or cssDir
cssExt = input(f"S/CSS file extension \t(default: {cssExt}):\t") or cssExt
diffFileName = input(f"Diff file name \t\t(default: {diffFileName}):\t") or diffFileName
useBothClasses = input(f"Keep both classes? Y/N \t(default: {useBothClasses}):\t") or useBothClasses

print("\nUsing values:")
print("S/CSS directory:", cssDir)
print("S/CSS file extension:", cssExt)
print("Diff file name:", diffFileName)
print("Keep both classes:", useBothClasses)

input("\nPress enter to continue or Ctrl+C to cancel.")

def readFromFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read()

def writeToFile(fileName, content):
    with open(fileName, "w", encoding="utf-8") as file:
        file.write(content)

def getReplacePairs():
    with open(os.path.join(diffFileName), "r", encoding="utf-8") as diffFile:
        normalised = diffFile.read()
        # Remove start of minus diff
        regex = re.compile('[-] .*: "')
        normalised = regex.sub('', normalised)
        # Remove end of minus diff and start of plus diff
        regex = re.compile('",\n\+.*: "')
        normalised = regex.sub(',', normalised)
        # Remove remaining quotes
        regex = re.compile('",')
        normalised = regex.sub('', normalised)
    pairs = [line.split(",") for line in normalised.splitlines()]
    # print(pairs[:10])
    return pairs

def main():
    replaceCount = 0
    classPairs = getReplacePairs()

    cssFileNames = glob.glob(os.path.join("..", cssDir, "**", cssExt), recursive=True)
    for cssFileName in cssFileNames:
        # print(cssFileName)
        cssString = readFromFile(cssFileName)

        for pair in classPairs:
            oldCssString = cssString
            bothClasses = f":is(.{pair[0]}, .{pair[1]})"

            if bothClasses in cssString:
                continue
            else:
                if useBothClasses.upper() == "Y":
                    cssString = cssString.replace(f".{pair[0]}", bothClasses)
                else:
                    cssString = cssString.replace(pair[0], pair[1])
            if oldCssString != cssString:
                replaceCount += 1

        writeToFile(cssFileName, cssString)

    print(f"\nReplaced {replaceCount} classes in {len(cssFileNames)} files.")

main()