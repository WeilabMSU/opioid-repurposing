# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 15:43:10 2019

@author: fenghon1
"""

import numpy as np
import argparse
import pandas as pd
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn import metrics 
import scipy.stats as stats
import os
from statistics import mean
import pickle
import sys


def receptor_map(receptor):
    if receptor == 'MOR':
        return 'OPRM1'
    elif receptor == 'DOR':
        return 'OPRD1'
    elif receptor == 'KOR':
        return 'OPRK1'
    elif receptor == 'hERG':
        return 'hERG'

receptors = ['MOR','KOR','DOR','hERG']

fps = ['TF','ecfp4']
preds = []
for receptor in receptors:
    pred_results = []
    for fp in fps:
        if fp =='TF':
            features_name = 'features/test-TF.npy'
            features = np.load(features_name)
        elif fp =='ecfp4':
            features_test = 'features/test-ecfp4.csv'
            features = pd.read_csv(features_test,header=None)

        predictor = pickle.load(open("models/LS-model-%s-%s-c0.sav"%(receptor_map(receptor),fp),'rb'))
        res = predictor.predict(features)
        pred_results.append(res)
    pred = np.mean(pred_results,axis=0)
    preds.append(pred)

preds = np.transpose(preds).tolist()

if not os.path.exists('predictions'):
    os.mkdir('predictions')
    
df = pd.DataFrame(preds,columns=receptors)
df.round(2).to_csv('predictions/preds.csv',index=False)


