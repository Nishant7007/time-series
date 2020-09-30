from liveLoadSeries import *
import pandas as pd
import numpy as np
from datetime import timedelta
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import sklearn


n_estimators = [int(x) for x in np.linspace(start = 2, stop = 10, num = 5)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(2, 8, num =4)]
max_depth.append(None)
min_samples_split = [int(x) for x in range(2,4)]
min_samples_leaf = [int(x) for x in range(2,4)]
bootstrap = [True,False]
#oob_score=[True,False]
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
rf = RandomForestClassifier()

def Normalise(arr):
  '''
  Normalise each sample
  '''
  m = arr.mean()
  am = arr.min()
  aM = arr.max()
  arr -= m
  arr /= (aM - am)
  return arr


azadpurArrivalOld = Normalise(azadpurArrivalOld)
kalyaniArrivalOld = Normalise(kalyaniArrivalOld)
bangaloreArrivalOld = Normalise(bangaloreArrivalOld)
bijnaurArrivalOld =Normalise(bijnaurArrivalOld)
lasalgaonArrivalOld =Normalise(lasalgaonArrivalOld)

azadpurPriceOld = Normalise(azadpurPriceOld)
kalyaniPriceOld = Normalise(kalyaniPriceOld)
bangalorePriceOld = Normalise(bangalorePriceOld)
bijnaurPriceOld = Normalise(bijnaurPriceOld)
lasalgaonPriceOld = Normalise(lasalgaonPriceOld)

delhiRetailOld = Normalise(delhiRetailOld)
kolkataRetailOld = Normalise(kolkataRetailOld)
bangaloreRetailOld = Normalise(bangaloreRetailOld)
lucknowRetailOld = Normalise(lucknowRetailOld)
mumbaiRetailOld = Normalise(mumbaiRetailOld)

azadpurArrivalNew = Normalise(azadpurArrivalNew)
kalyaniArrivalNew = Normalise(kalyaniArrivalNew)
bangaloreArrivalNew = Normalise(bangaloreArrivalNew)
bijnaurArrivalNew =Normalise(bijnaurArrivalNew)
lasalgaonArrivalNew =Normalise(lasalgaonArrivalNew)

azadpurPriceNew = Normalise(azadpurPriceNew)
kalyaniPriceNew = Normalise(kalyaniPriceNew)
bangalorePriceNew = Normalise(bangalorePriceNew)
bijnaurPriceNew = Normalise(bijnaurPriceNew)
lasalgaonPriceNew = Normalise(lasalgaonPriceNew)

delhiRetailNew = Normalise(delhiRetailNew)
kolkataRetailNew = Normalise(kolkataRetailNew)
bangaloreRetailNew = Normalise(bangaloreRetailNew)
lucknowRetailNew = Normalise(lucknowRetailNew)
mumbaiRetailNew = Normalise(mumbaiRetailNew)




#print(delhiAnomaly)


def finalModel()




