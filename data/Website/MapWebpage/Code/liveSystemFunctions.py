import pickle
from liveWholesaleCrawler import *
monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


d = pickle.load(open('myDicts.p','rb'))

#print(d)

def wholesaleDataCrawler(Dict):
    commodities, centres, months, years = ([],[],[],[])
    for com in Dict.keys():
        for k in Dict[com].keys():
            commodities.append(com)
            centres.append(k)
            months.append(Dict[com][k][0])
            years.append(Dict[com][k][1])
    wholesaleResult = extractWholesaleData(commodities, centres, months, years)
    print('wholesaleResult')
    print(wholesaleResult)
    newDict = Dict
    if(len(wholesaleResult)!=0):
        for com in wholesaleResult.keys():
            if((wholesaleResult[com][1] == 1) | (wholesaleResult[com][1] == 2)):
                indexValue = monthList.index(wholesaleResult[com][2])
                if((indexValue + 1) == len(monthList)):
                    m = monthList[0]
                    y = wholesaleResult[com][3] + 1
                else:
                    m = monthList[indexValue+1]
                    y = wholesaleResult[com][3]
            else:
                m = wholesaleResult[com][2]
                y = wholesaleResult[com][3]
            k = wholesaleResult[com][0]
            newDict[com][k] = [m,y]
    return newDict

