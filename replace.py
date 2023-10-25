import re, os, glob

def getParamsFromUser():
    cssDir = "themes"
    cssExt = "*.scss"
    oldDiffFileName = "olddiff.txt"
    newDiffFileName = "newdiff.txt"

    # Comment out this section if you want to just hardcode the values.
    print("Leave blank to use default values.")
    cssDir = input(f"S/CSS directory \t(default: {cssDir}):\t") or cssDir
    cssExt = input(f"S/CSS file extension \t(default: {cssExt}):\t") or cssExt
    oldDiffFileName = input(f"Old diff file name \t(default: {oldDiffFileName}):\t") or oldDiffFileName
    newDiffFileName = input(f"New diff file name \t(default: {newDiffFileName}):\t") or newDiffFileName

    print("\nUsing values:")
    print("S/CSS directory:\t", cssDir)
    print("S/CSS file extension:\t", cssExt)
    print("Old diff file name:\t", oldDiffFileName)
    print("New diff file name:\t", newDiffFileName)

    input("\nPress enter to continue or Ctrl+C to cancel.")

    return cssDir, cssExt, oldDiffFileName, newDiffFileName

def readFromFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read()

def writeToFile(fileName, content):
    with open(fileName, "w", encoding="utf-8") as file:
        file.write(content)

def getDiffClassPairs(diffFileName):
    # Remove start of minus diff
    regex = re.compile('[-] .*: "')
    normalised = regex.sub('', readFromFile(diffFileName))
    # Remove end of minus diff and start of plus diff
    regex = re.compile('",\n\+.*: "')
    normalised = regex.sub(',', normalised)
    # Remove remaining quotes
    regex = re.compile('",')
    normalised = regex.sub('', normalised)
    classPairs = [line.split(",") for line in normalised.splitlines()]
    # print(classPairs[:10])
    return classPairs

def getTxtClassPairs(diffFileName):
    # Format:
    # oldClassName-123456
    # newClassName-654321
    # Repeat for every updated class
    diffFileContent = readFromFile(diffFileName).splitlines()
    classPairs = [[oldClass, newClass] for oldClass, newClass in zip(diffFileContent[::2], diffFileContent[1::2])]
    # print(classPairs[:10])
    return classPairs

def replaceClasses(cssString, oldClassPairs, newClassPairs):
    replaceCount = 0

    # Replace ancient classes or :is(ancient, old) with old classes
    for ancientClass, oldClass in oldClassPairs:
        oldCssString = cssString
        oldCssPair = f":is(.{ancientClass}, .{oldClass})"

        cssString = cssString.replace(oldCssPair, f".{oldClass}")
        cssString = cssString.replace(ancientClass, oldClass)

        if oldCssString != cssString:
            replaceCount += 1

    # Replace old classes with new classes
    for oldClass, newClass in newClassPairs:
        cssString = cssString.replace(oldClass, newClass)

        if oldCssString != cssString:
            replaceCount += 1

    return cssString, replaceCount

def main():
    cssDir, cssExt, oldDiffFileName, newDiffFileName = getParamsFromUser()

    oldClassPairs = getTxtClassPairs(oldDiffFileName)
    newClassPairs = getTxtClassPairs(newDiffFileName)

    totalReplaceCount = 0

    cssFileNames = glob.glob(os.path.join("..", cssDir, "**", cssExt), recursive=True)
    for cssFileName in cssFileNames:
        # print(cssFileName)
        cssString = readFromFile(cssFileName)

        # Convert ancient classes and :is(ancient, old) class pairs to new classes
        cssString, replaceCount = replaceClasses(cssString, oldClassPairs, newClassPairs)
        totalReplaceCount += replaceCount

        # Write to file
        writeToFile(cssFileName, cssString)

    print(f"\nReplaced {totalReplaceCount} classes in {len(cssFileNames)} files.")

main()