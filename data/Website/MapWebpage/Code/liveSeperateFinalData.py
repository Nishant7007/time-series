import pickle as pkl
import pandas as pd
from liveInformation import *

d = pkl.load(open('myDicts.p','rb'))
#print(d)

commodityList = list(d['commodity'].keys())

def makeArrivalFiles():
        for commodity in commodityList:
                s = commodity+'_Mandis'
                states = list(d[s].keys())
                for state in states:
                        MandisList = d[s][state]
                        #print(MandisList)
                        fileToOpen = commodity + str('_') + state.replace(' ','') + 'Arrival.csv'
                        df = pd.read_csv('../Data/Processed/Arrival/'+str(fileToOpen),header=None)
                        #print(df)
                        for mandiname in MandisList:
                                try:
                                        #print(df.head(2))
                                        mandicode = dict_mandiname_mandicode[mandiname][0]
                                        dfArrival = df[df[1] == mandicode]
                                        dfArrival1 = dfArrival[[0,2]]
                                        dfArrival1.reset_index(inplace = True, drop = True)
                                        dfArrival1.columns = [0,1]
                                        fileToSave = '../Data/Final/Arrival/' + str(commodity.replace(' ','')) + '_' + str(state.replace(' ','')) + '_' + str(mandiname.replace(' ',''))+'_Arrival.csv'
                                        dfArrival1.to_csv(fileToSave,header=None,index = False)
                                except:
                                        print('sorry')
                                        continue
                print(" ")


def makePriceFiles():
        for commodity in commodityList:
                s = commodity+'_Mandis'
                states = list(d[s].keys())
                for state in states:
                        MandisList = d[s][state]
                        fileToOpen = commodity + str('_') + state.replace(' ','') + 'Price.csv'
                        df = pd.read_csv('../Data/Processed/Price/'+str(fileToOpen),header=None)
                        #print(df)
                        for mandiname in MandisList:
                                try:
                                        #print(df.head(2))
                                        mandicode = dict_mandiname_mandicode[mandiname][0]
                                        dfPrice = df[df[1] == mandicode]
                                        dfPrice1 = dfPrice[[0,2]]
                                        dfPrice1.reset_index(inplace = True, drop = True)
                                        dfPrice1.columns = [0,1]
                                        #print(commodity,state,mandiname)
                                        #print(dfPrice1.head())
                                        fileToSave = '../Data/Final/Price/' + str(commodity.replace(' ','')) + '_' + str(state.replace(' ','')) + '_' + str(mandiname.replace(' ',''))+'_Price.csv'
                                        dfPrice1.to_csv(fileToSave,header=None,index = False)
                                except:
                                        print('sorry')
                                        continue


