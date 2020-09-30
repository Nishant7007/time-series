from os import listdir,rename
from os.path import join
def editNamesFunction(directory):
	files = listdir(directory)
	for file in files:
		fileName = join(directory,file)
		newName = join(directory,file.replace(' ',''))
		rename(fileName,newName)

#print('editing done')
