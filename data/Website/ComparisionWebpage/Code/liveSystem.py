import pickle


print('LOADING ALL SCRIPTS')

from nameChanger import *
from liveSystemFunctions import *
from liveFormatWholesaleData import *
from liveProcessData import *


print('LOADING ALL DICTIONARIES AND DECLARING GLOBAL VARIALBES')
d = pickle.load(open('myDicts.p','rb'))
print('Data dictionary before all work')
#print(d)

wholesaleRawDirectory = '../Data/Original/WholesaleRaw'
wholesaleDirectory = '../Data/Original/Wholesale'
processedWholesaleDirectory = '../Data/Processed/Wholesale'

print('Download Wholesale Data')
d['MonthsDict'] = wholesaleDataCrawler(d['MonthsDict'])
#print(d)

print('remove extra mynewdata_ from whoesale files')
nameChangerFunction(wholesaleRawDirectory)

print('formatting the wholesalefiles')
formatData(wholesaleRawDirectory)


CommodityStateFiles = []
for k in d['commodityStates'].keys():
        for x in d['commodityStates'][k]:
                CommodityStateFiles.append(k+'/'+x)

print('Processing wholesale data')
#print(CommodityStateFiles)
processWholesaleData(CommodityStateFiles)



















print('Data dictionary after all work')
#print(d)
print('Dumping Data Dictionary')
file = open('myDicts.p', 'wb')
pickle.dump(d,file)

