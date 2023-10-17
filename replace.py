import re, os, glob

cssDir = "scss"
cssExt = "*.scss"
diffFileName = "diff.diff"

# Comment out this section if you want to just hardcode the values.
print("Leave blank to use default values.")
cssDir = input("S/CSS directory \t(default: scss):\t") or cssDir
cssExt = input("S/CSS file extension \t(default: *.scss):\t") or cssExt
diffFileName = input("Diff file name \t\t(default: diff.diff):\t") or diffFileName

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
            cssString = cssString.replace(pair[0], pair[1])
            if cssString != cssString:
                replaceCount += 1

        writeToFile(cssFileName, cssString)

    print("Replaced", replaceCount, "classes in", len(cssFileNames), "files.")

main()