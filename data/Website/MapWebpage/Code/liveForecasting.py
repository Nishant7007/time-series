
import pickle as pkl
import pandas as pd
from liveInformation import *
import datetime
import calendar
import numpy as np
from pmdarima.preprocessing import FourierFeaturizer
import pmdarima as pm


date_str = '2016-01-01'
startDate = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()


d = pkl.load(open('myDicts.p','rb'))

commodityList = list(d['commodity'].keys())



def forecastArrival(forecastingDict,d):
        for commodity in commodityList:
                s = commodity+'_Mandis'
                states = list(d[s].keys())
                if(commodity in forecastingDict.keys()):
                    for state in states:
                            if(state == forecastingDict[commodity][0]):
                                if(forecastingDict[commodity][1] ==1 ):
                                    MandisList = d[s][state]
                                    for mandiname in MandisList:
                                            try:
                                                    fileToOpen = '../Data/Final/Arrival/' + str(commodity.replace(' ','')) + '_' + str(state.replace(' ','')) + '_' + str(mandiname.replace(' ',''))+'_Arrival.csv'
                                                    print(fileToOpen)
                                                    df = pd.read_csv(fileToOpen,header = None)
                                                    maxDate = (df[0].max()).split('-')
                                                    lastDate = calendar.monthrange(int(maxDate[0]),int(maxDate[1]))
                                                    endDate = datetime.date(int(maxDate[0]),int(maxDate[1]),lastDate[1])
                                                    df.index = df[0]
                                                    df = df[[1]]
                                                    df = df.loc[~df.index.duplicated(keep='first')]
                                                    idx = pd.date_range(startDate,endDate)
                                                    df.index = pd.DatetimeIndex(df.index)
                                                    df = df.reindex(idx, fill_value=0)
                                                    df[1] = df[1].replace(0.0,np.nan)
                                                    df[1] = (df[1].interpolate(method = 'linear').bfill()).ffill()
                                                    daysToForecast = 30
                                                    series_train = np.squeeze(df.values)
                                                    trans = FourierFeaturizer(365.25, 1)
                                                    y_prime, exogen = trans.fit_transform(series_train)
                                                    exogen = exogen.mul(pd.Series(series_train),axis=0)
                                                    futureExog =  trans.transform(y = series_train, n_periods = daysToForecast)
                                                    model=pm.arima.auto_arima(series_train, exogenous = exogen, start_p=0, d=None, start_q=0, max_p=3, max_d=1, max_q=3,start_P=0, D=None, start_Q=0, max_P=2, max_D=1, max_Q=2,suppress_warnings =True,seasonal=True,max_order=5,m=7,stepwise=True,initialization='approximate_diffuse',enforce_stationarity=False)
                                                    model.fit(series_train)
                                                    pred = model.predict(daysToForecast,exogenous = futureExog)
                                                    series = (np.concatenate((series_train , np.array(pred)),axis = 0))
                                                    dk=pd.DataFrame(series)
                                                    dk['date']=pd.date_range('2016-01-01',periods=len(series))
                                                    dk.index = dk['date']
                                                    dk = dk[0]
                                                    dk.to_csv('../Data/Results/Arrival/'+str(commodity.replace(' ','')) + '_' + str(state.replace(' ','')) + '_' + str(mandiname.replace(' ',''))+'_Arrival.csv',header = False)
                                            except:
                                                    continue


def forecastPrice(forecastingDict,d):
        for commodity in commodityList:
                s = commodity+'_Mandis'
                states = list(d[s].keys())
                if(commodity in forecastingDict.keys()):
                    for state in states:
                        if(state == forecastingDict[commodity][0]):
                            if(forecastingDict[commodity][1] ==1 ):
                                MandisList = d[s][state]
                                for mandiname in MandisList:
                                        try:
                                                fileToOpen = '../Data/Final/Price/' + str(commodity.replace(' ','')) + '_' + str(state.replace(' ','')) + '_' + str(mandiname.replace(' ',''))+'_Price.csv'
                                                print(fileToOpen)
                                                df = pd.read_csv(fileToOpen,header = None)
                                                maxDate = (df[0].max()).split('-')
                                                lastDate = calendar.monthrange(int(maxDate[0]),int(maxDate[1]))
                                                endDate = datetime.date(int(maxDate[0]),int(maxDate[1]),lastDate[1])
                                                df.index = df[0]
                                                df = df[[1]]
                                                df = df.loc[~df.index.duplicated(keep='first')]
                                                idx = pd.date_range(startDate,endDate)
                                                df.index = pd.DatetimeIndex(df.index)
                                                df = df.reindex(idx, fill_value=0)
                                                df[1] = df[1].replace(0.0,np.nan)
                                                df[1] = (df[1].interpolate(method = 'linear').bfill()).ffill()
                                                daysToForecast = 30
                                                series_train = np.squeeze(df.values)
                                                trans = FourierFeaturizer(365.25, 1)
                                                y_prime, exogen = trans.fit_transform(series_train)
                                                exogen = exogen.mul(pd.Series(series_train),axis=0)
                                                futureExog =  trans.transform(y = series_train, n_periods = daysToForecast)
                                                model=pm.arima.auto_arima(series_train, exogenous = exogen, start_p=0, d=None, start_q=0, max_p=3, max_d=1, max_q=3,start_P=0, D=None, start_Q=0, max_P=2, max_D=1, max_Q=2,suppress_warnings =True,seasonal=True,max_order=5,m=7,stepwise=True, initialization='approximate_diffuse',enforce_stationarity=False)
                                                model.fit(series_train)
                                                pred = model.predict(daysToForecast,exogenous = futureExog)
                                                series = (np.concatenate((series_train , np.array(pred)),axis = 0))
                                                dk=pd.DataFrame(series)
                                                dk['date']=pd.date_range('2016-01-01',periods=len(series))
                                                dk.index = dk['date']
                                               #print(dk)
                                                dk = dk[0]
                                                dk.to_csv('../Data/Results/Price/'+str(commodity.replace(' ','')) + '_' + str(state.replace(' ','')) + '_' + str(mandiname.replace(' ',''))+'_Price.csv',header = False)                     
                                        except:
                                                continue
                            else:
                                print('comm aval but not state')


