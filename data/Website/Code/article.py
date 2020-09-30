import os
def getFileNameWithString(dirName,stringToFind):
    # reate a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            getFileNameWithString(fullPath,stringToFind)
        else:
            
            # if(fullPath.endswith('.ipynb')):
            #     print(fullPath)
            if(fullPath.endswith('.py')):
                with open(fullPath,'rb') as f:
                    contents = f.read()
                    #print(type(contents))
                    if (bytes(stringToFind,encoding='utf8')) in contents:
                        print(fullPath)
                
    return allFiles

allFiles = getFileNameWithString('../Code',"listdir")

print(allFiles)



