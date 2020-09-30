import pickle

from nameChanger import *
from liveFormatWholesaleData import *
from liveProcessData import *
from editNames import *
from liveSeperateFiles import *
from liveSeperateFinalData import *
from liveForecasting import *
from liveSystemFunctions import *

print('Loading Data Dictionary')
d = pickle.load(open('myDicts.p','rb'))

print('Data dictionary before all work')
print(d)

wholesaleRawDirectory = '../Data/Original/WholesaleRaw'
wholesaleDirectory = '../Data/Original/Wholesale'
processedWholesaleDirectory = '../Data/Processed/Wholesale'

CommodityStateFiles = []
for k in d['commodityFiles'].keys():
        for x in d['commodityFiles'][k]:
                CommodityStateFiles.append(k+'/'+x)


print('Download Wholesale Data')
d['MonthsDict'] = wholesaleDataCrawler(d['MonthsDict'])

print('remove extra .csv from whoesale files')
nameChangerFunction(wholesaleRawDirectory)

print('formatting the wholesalefiles')
formatData(wholesaleRawDirectory)

print('Processing wholesale data')
processWholesaleData(CommodityStateFiles)

print('edit names of processed wholesale files')
editNamesFunction(processedWholesaleDirectory)

print('Seperating Price and Arrival Files')
seperateFiles()

print('Seperate Final Price and Arrival Data')
makeArrivalFiles()
makePriceFiles()
print('Final Price and Arrival Data Seperated')

forecastingDict = pkl.load(open('newdata.p','rb'))
forecastingDict = {k.replace(' ', ''): v for k, v in forecastingDict.items()}

print('Forecasting Arrival Data')
forecastArrival(forecastingDict,d)

print('Forecasting Price Data')
forecastPrice(forecastingDict,d)

print('Data dictionary after all work')
print(d)
print('Dumping Data Dictionary')
file = open('myDicts.p', 'wb')
pickle.dump(d,file)
