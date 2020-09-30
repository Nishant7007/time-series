from os import listdir
import os


commodityStates = {}
for folder in listdir('../Data/Original'):
	l = []
	for subfolder in listdir(os.path.join('../Data/Original',folder)):
		l.append(subfolder)
	commodityStates[folder] = l
print(commodityStates)
