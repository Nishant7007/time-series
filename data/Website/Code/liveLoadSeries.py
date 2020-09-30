import pickle
import pandas as pd 
from datetime import datetime
import numpy as np
from os import listdir
from datetime import datetime, timedelta

cts = pickle.load(open ("myDicts.p","rb"))

date_format = "%Y-%m-%d"
startDate = "2006-01-01"

myDicts = pickle.load( open ("myDicts.p", "rb"))


def loadMandiSeries(name):
	df = pd.read_csv('../Data/Results/Actual/'+name+'Price.csv',header=None)
	df = df[df[0]>=startDate]
	df.drop_duplicates(subset = 0 , inplace = True)
	df.reset_index(inplace = True , drop = True)
	recent_date = df[0].max()
	l = (datetime.strptime(recent_date, date_format) - datetime.strptime('2006-01-01', date_format)).days	
	idx = pd.date_range('2006-01-01', periods = l)
	df.index = pd.DatetimeIndex(df[0])
	df = df[[1]]
	df = df.reindex(idx, fill_value = 0)
	df.replace(0,np.nan,inplace = True)
	df = df.interpolate(method = 'linear',limit_direction = 'both')
	df = df[[1]]
	return df


def loadAllMandiSeries(Dicts):
	mandiDict = {}
	for v in Dicts.values():
		name = v[0]
		#print(name)
		mandiDict[name] = loadMandiSeries(name)
	return (mandiDict)	

def loadArrivalSeries(name):
	df = pd.read_csv('../Data/Results/Actual/'+name+'Arrival.csv',header=None)
	df = df[df[0]>=startDate]
	df.drop_duplicates(subset = 0, inplace = True)
	df.reset_index(inplace = True, drop = True)
	recent_date = df[0].max()
	l = (datetime.strptime(recent_date, date_format) - datetime.strptime('2006-01-01', date_format)).days	
	idx = pd.date_range('2006-01-01', periods = l)
	df.index = pd.DatetimeIndex(df[0])
	df = df[[1]]
	df = df.reindex(idx, fill_value = 0)
	df.replace(0,np.nan,inplace = True)
	df = df.interpolate(method = 'linear',limit_direction = 'both')
	df = df[[1]]
	return df


def loadAllArrivalSeries(Dicts):
	arrivalDict = {}
	for v in Dicts.values():
		name = v[0]
		arrivalDict[name] = loadArrivalSeries(name)
	return (arrivalDict)	


def loadRetailSeries(name):
        df = pd.read_csv('../Data/Results/Actual/'+name+'Retail.csv',header=None)
        df = df[df[0]>=startDate]
        df.drop_duplicates(subset = 0 , inplace = True)
        df.reset_index(inplace = True , drop = True)
        recent_date = df[0].max()
        l = (datetime.strptime(recent_date, date_format) - datetime.strptime('2006-01-01', date_format)).days
        idx = pd.date_range('2006-01-01', periods = l)
        df.index = pd.DatetimeIndex(df[0])
        df = df[[1]]
        df = df.reindex(idx, fill_value = 0)
        df.replace(0,np.nan,inplace = True)
        df = df.interpolate(method = 'linear',limit_direction = 'both')
        df = df[[1]]
        return df


def loadAllRetailSeries(Dicts):
        retailDict = {}
        for v in Dicts.values():
                name = v[0]
                retailDict[name] = loadRetailSeries(name)
        return (retailDict)


def AnomalySeries(dicts):
	#print("dicts",dicts)
	anomalyDict = {}
	for v in dicts.values():
		name = v[0]
		#print(name)
		fileName = '../Data/Anomaly/'+str(name)+'Anomalies.csv'
		df = pd.read_csv(fileName,header=None,names =['start','end','class'])
		df['class'] = df['class'].str.lower()
		#df['class'] = df['class'].replace(['fuel','transport','supply'],'weather')
		df = df[(df['class'] == 'weather') | (df['class'] == 'hoarding') | (df['class'] == 'supply') | (df['class'] == 'no')]
		anomalyDict[name] = df
	return anomalyDict


retailDict = loadAllRetailSeries(myDicts['centreCodes'])
priceDict = loadAllMandiSeries(myDicts['mandiCodes'])
arrivalDict = loadAllArrivalSeries(myDicts['mandiCodes'])

anomalyDict = AnomalySeries(myDicts['centreCodes'])

azadpurArrival = arrivalDict.get('Azadpur')
kalyaniArrival = arrivalDict.get('Kalyani')
bangaloreArrival = arrivalDict.get('Bangalore')
bijnaurArrival = arrivalDict.get('Bijnaur')
lasalgaonArrival = arrivalDict.get('Lasalgaon')


azadpurPrice = priceDict.get('Azadpur')
kalyaniPrice = priceDict.get('Kalyani')
bangalorePrice = priceDict.get('Bangalore')
bijnaurPrice = priceDict.get('Bijnaur')
lasalgaonPrice = priceDict.get('Lasalgaon')



delhiRetail = retailDict.get('DELHI')
kolkataRetail = retailDict.get('KOLKATA')
bangaloreRetail = retailDict.get('Bengaluru')
lucknowRetail = retailDict.get('LUCKNOW')
mumbaiRetail = retailDict.get('MUMBAI')


#print(anomalyDict)
delhiAnomaly = anomalyDict['DELHI']
lucknowAnomaly = anomalyDict['LUCKNOW']
kolkataAnomaly = anomalyDict['KOLKATA']
bangaloreAnomaly = anomalyDict['Bengaluru']
mumbaiAnomaly = anomalyDict['MUMBAI']


delhiDate = min(azadpurArrival.index.max(),azadpurPrice.index.max(),delhiRetail.index.max())
kolkataDate = min(kalyaniArrival.index.max(),kalyaniPrice.index.max(),kolkataRetail.index.max())
bangaloreDate = min(bangaloreArrival.index.max(),bangalorePrice.index.max(),bangaloreRetail.index.max())
lucknowDate = min(bijnaurArrival.index.max(),bijnaurPrice.index.max(),lucknowRetail.index.max())
mumbaiDate = min(lasalgaonArrival.index.max(),lasalgaonPrice.index.max(),mumbaiRetail.index.max())


#print(delhiDate,kolkataDate,bangaloreDate,lucknowDate,mumbaiDate)
#print(delhiDate-timedelta(30))


