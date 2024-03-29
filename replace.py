import re, os, glob, urllib.request

def getParamsFromUser():
    cssDir = "themes"
    cssExt = "css"
    useLocalDiff = "Y"
    diffFile = "Changes.txt"
    diffUrl = "https://raw.githubusercontent.com/SyndiShanX/Update-Classes/main/Changes.txt"

    # Comment out this section if you want to just hardcode the values.
    print("Leave blank to use default values.")
    cssDir = input(f"Themes directory \t(default: {cssDir}):\t") or cssDir
    cssExt = input(f"File extension \t\t(default: {cssExt}):\t\t") or cssExt
    useLocalDiff = input(f"Y/N use local diff\t(default: {useLocalDiff}):\t\t") or useLocalDiff
    if useLocalDiff.lower() == "y":
        useLocalDiff = True
        diffUrl = diffFile
        diffUrl = input(f"Diff file location\t(default: {diffUrl}):\t") or diffUrl
    else:
        useLocalDiff = False
        diffUrl = input(f"Diff URL \t\t(default: {diffUrl}):\t") or diffUrl

    print("\nUsing values:")
    print(f"Themes directory:\t{cssDir}")
    print(f"File extension:\t\t{cssExt}")
    print(f"Use local diff:\t\t{useLocalDiff}")
    if useLocalDiff == True:
        print(f"Diff file location:\t{diffUrl}")
    else:
        print(f"Diff URL:\t\t{diffUrl}")

    cssFileNames = glob.glob(os.path.join("..", cssDir, "**", "*." + cssExt), recursive=True)

    print(f"\nFound {len(cssFileNames)} {cssExt} files in {cssDir}.")
    input("Press enter to continue or Ctrl+C to cancel.")

    return useLocalDiff, diffUrl, cssFileNames

def readFromFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read()

def writeToFile(fileName, content):
    with open(fileName, "w", encoding="utf-8") as file:
        file.write(content)

def getClassPairs(useLocalDiff, diffUrl):
    if useLocalDiff == True:
        diffFileContent = readFromFile(diffUrl).splitlines()
    else:
        diffFileContent = urllib.request.urlopen(diffUrl).read().decode("utf-8").splitlines()
    classPairs = [[oldClass, newClass] for oldClass, newClass in zip(diffFileContent[::2], diffFileContent[1::2])]
    return classPairs

def replaceClasses(cssString, classPairs):
    replaceCount = 0

    for oldClass, newClass in classPairs:
        oldCssString = cssString

        cssPair = f":is(.{oldClass}, .{newClass})"
        cssString = cssString.replace(cssPair, f".{oldClass}").replace(oldClass, newClass)

        if oldCssString != cssString:
            replaceCount += 1

    return cssString, replaceCount

def main():
    useLocalDiff, diffUrl, cssFileNames = getParamsFromUser()
    classPairs = getClassPairs(useLocalDiff, diffUrl)

    totalReplaceCount = 0
    totalFilesChangedCount = 0

    for cssFileName in cssFileNames:
        # Get CSS file content
        cssString = readFromFile(cssFileName)

        # Convert old classes and old class pairs to new classes.
        cssString, replaceCount = replaceClasses(cssString, classPairs)
        if replaceCount > 0:
            totalFilesChangedCount += 1
            totalReplaceCount += replaceCount

        # Write CSS to file
        writeToFile(cssFileName, cssString)

    print(f"\nReplaced {totalReplaceCount} classes in {totalFilesChangedCount} files.")

main()