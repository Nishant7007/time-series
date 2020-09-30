
from datetime import datetime
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
from os import listdir
import datetime as datetime
from os import scandir
import pickle
from liveInformation import *

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

d = pickle.load(open('myDicts.p','rb'))
#print(d)

mandi_info = pd.read_csv('../Data/Information/mandis.csv')
dict_centreid_mandicode = mandi_info.groupby('centreid')['mandicode'].apply(list).to_dict()
dict_mandicode_mandiname = mandi_info.groupby('mandicode')['mandiname'].apply(list).to_dict()
dict_mandicode_statecode = mandi_info.groupby('mandicode')['statecode'].apply(list).to_dict()
dict_mandicode_centreid = mandi_info.groupby('mandicode')['centreid'].apply(list).to_dict()
dict_mandiname_mandicode = mandi_info.groupby('mandiname')['mandicode'].apply(list).to_dict()

centre_info = pd.read_csv('../Data/Information/centres.csv')
dict_centreid_centrename = centre_info.groupby('centreid')['centrename'].apply(list).to_dict()
dict_centreid_statecode = centre_info.groupby('centreid')['statecode'].apply(list).to_dict()
dict_statecode_centreid = centre_info.groupby('statecode')['centreid'].apply(list).to_dict()

state_info = pd.read_csv('../Data/Information/states.csv')
dict_statecode_statename = state_info.groupby('statecode')['state'].apply(list).to_dict()
dict_statename_statecode = state_info.groupby('state')['statecode'].apply(list).to_dict()


def processWholesaleData(states):
        print('states are ',states)
        for state in states:
                files = [f for f in listdir('../Data/Original/Wholesale/'+str(state)) if not f.startswith('.') ]
                files.sort()
                code=-1
                fileName = state.replace('/','_')
                newfile = open('../Data/Processed/Wholesale/'+str(fileName)+'.csv','w')
                lines = []
                for j in range(len(files)):
                        file=files[j]
                        with open('../Data/Original/Wholesale/'+str(state)+'/'+file) as f:
                                content=f.readlines()
                                for i in range(1,len(content)):
                                        try:
                                                temp = content[i].strip().split(',')
                                                mandi = temp[0]
                                                date = temp[1]
                                                if(len(date) == 8):
                                                        date = date[6] +'20'+date[6:]
                                                date = datetime.datetime.strptime(date,'%d/%m/%Y').strftime('%Y-%m-%d')
                                                arrival = temp[2]
                                                variety = temp[3]
                                                minp = temp[4]
                                                maxp = temp[5]
                                                modalp = temp[6]
                                                if not isInt(minp):
                                                        minp = '0'
                                                if not isInt(maxp):
                                                        maxp = '0'
                                                if not isInt(modalp):
                                                        modalp = '0'
                                                if mandi != '':
                                                        if mandi in dict_mandiname_mandicode.keys():
                                                                code = dict_mandiname_mandicode[mandi]
                                                        else:
                                                                code = -1
                                                if code != -1 and minp != 'NR':
                                                       mystr=date+','+str(code[0])+','+arrival+',NR,'+variety+','+minp+','+maxp+','+modalp+'\n'
                                                       lines.append(mystr)
                                        except:
                                                continue
                lines.sort()
                i=0
                for line in lines:
                        i+=1
                        newfile.write(line)
                newfile.close()
        print('Processing completed')


