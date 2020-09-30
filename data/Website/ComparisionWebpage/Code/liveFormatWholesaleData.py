import os
import pandas as pd
import datetime
from findAllFiles import *

def formatData(directory):
    dirs =  getFileNameWithString(directory)
    for file in dirs:
        if(file.endswith('.csv')):
            newFile = file.replace('WholesaleRaw','Wholesale')
            df = pd.read_csv(str(file),header=None, error_bad_lines = False, warn_bad_lines = False)
            df.ffill(inplace = True)
            #print(newFile)
            df.to_csv(str(newFile),header=False,index=False)


