import os
allFiles = []
def getDirectoryNameWithString(dirName):
    listOfDirectories = os.listdir(dirName)
    for entry in listOfDirectories:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            if('git' not in fullPath):
                allFiles.append(fullPath)
                getDirectoryNameWithString(fullPath)
    return allFiles

