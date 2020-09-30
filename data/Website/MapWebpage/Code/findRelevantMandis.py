import pandas as pd
import pickle as pkl

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
dict_centrename_centreid = centre_info.groupby('centrename')['centreid'].apply(list).to_dict()


state_info = pd.read_csv('../Data/Information/states.csv')
dict_statecode_statename = state_info.groupby('statecode')['state'].apply(list).to_dict()
dict_statename_statecode = state_info.groupby('state')['statecode'].apply(list).to_dict()



dict_statename_mandicode = {}
for key,value in dict_statename_statecode.items():
    #print(key)
    val = value[0]
    l = []
    #print(val)
    for mcode,scode in dict_mandicode_statecode.items():
        #print(scode)
        if(val==scode[0]):
            #print(mcode)
            l.append(mcode)
    dict_statename_mandicode[key] = l

dict_commodity_mandi = (pkl.load(open('myDicts.p','rb')))['commodityStates']

#print(dict_commodity_mandi)

for commodity,state in dict_commodity_mandi.items():
	print('commodity',commodity)
	for s in state:
		print(s,commodity)
		for statename,mandicode in dict_statename_mandicode.items():
			if(s==statename.replace(' ','')):
				mandis = mandicode
				fileName = '../Data/Processed/Wholesale/'+str(commodity)+str(s)+'.csv'
				#print(fileName)
				df = pd.read_csv(fileName,header=None,usecols=[0,1,2,7])
				#print(df.head(3))
				for particularMandi in mandis:
					dfPar = df[df[1]==particularMandi]
					dxPar = dfPar.drop_duplicates(subset = 0)
					if((len(dxPar)/1634)*100>80):
						#print('Mandi Code: ',particularMandi,end=' ')
						print(dict_mandicode_mandiname[particularMandi][0],end=', ')
						#print((len(dfPar)/1642)*100,end=' ')
						#print(len(dfPar))
						#print(dfPar)
						#print(dfPar.tail(1))
				print('')
	print('')

#print(dict_commodity_mandi)
