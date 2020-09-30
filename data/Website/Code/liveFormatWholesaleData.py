import os
import pandas as pd
import datetime


def formatData():
	dirs = [f for f in os.listdir('../Data/Original/WholesaleRaw') if not f.startswith('.')]
	#print(dirs)
	for directory in dirs: 
		#print(directory)
		files = os.listdir('../Data/Original/WholesaleRaw/'+str(directory))
		for file in files:
			df = pd.read_csv('../Data/Original/WholesaleRaw/'+str(directory)+'/'+str(file),header=None, error_bad_lines = False, warn_bad_lines = False, engine='python')
			df.ffill(inplace = True)
			df.to_csv('../Data/Original/Wholesale/'+str(directory)+'/'+str(file),header=False,index=False)
	#print('fomatting done')
