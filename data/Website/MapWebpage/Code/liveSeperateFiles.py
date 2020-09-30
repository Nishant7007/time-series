from os import listdir
import pandas as pd


def seperateFiles():
        files = [f for f in listdir('../Data/Processed/Wholesale') if not f.startswith('.')]
        for file in files:
                #print(file)
                pricefile = '../Data/Processed/Price/' + file.replace('.csv','Price.csv')
                arrivalfile = '../Data/Processed/Arrival/' + file.replace('.csv','Arrival.csv')
                #print(pricefile,arrivalfile)
                try:
                        df = pd.read_csv('../Data/Processed/Wholesale/'+str(file),header=None)
                        df.index = df[0]
                        dfPrice = df[[1,7]]
                        dfArrival = df[[1,2]]
                        #print(dfPrice.head())
                        #print(dfArrival.head())
                        dfPrice.to_csv(pricefile,header=False)
                        dfArrival.to_csv(arrivalfile,header=False)
                        #print(dfPrice.head())
                except:
                        continue
        print('Price and Arrival Files Seperated')
