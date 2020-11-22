# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:35:18 2020

@author: SUDIP WALTER THOMAS
"""

import requests
import pandas
import scipy
import numpy as np
import sys
from scipy import stats

train_data_url = 'https://storage.googleapis.com/kubric-hiring/linreg_train.csv'
test_data_url = 'https://storage.googleapis.com/kubric-hiring/linreg_test.csv'

def predict_price(area) -> float:
    
    response = requests.get(train_data_url)
    response_content = response.content
    train_file = open('train.csv', 'wb')
    csv_file.write(response_content)
    csv_file.close()
    df = pandas.read_csv('train.csv', header= None).T
    head = df.iloc[0]
    df.drop([0], axis=0, inplace = True)
    df.columns = h
    x = np.asarray(df.area.astype('float'))
    y = np.asarray(df.price.astype('float'))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    y_pred = area*slope+intercept
    return y_pred

if __name__ == "__main__":
    from data import validation_data
    areas = np.array(list(validation_data.keys()))
    prices = np.array(list(validation_data.values()))
    predicted_prices = predict_price(areas)
    rmse = np.sqrt(np.mean(predicted_prices-prices)**2)
    try:
        assert rmse <170
    except AssertionError:
        print(f'RMSE: {rmse}, is higher than 170')
        sys.exit(1)
    print(f'RMSE = {rmse}, hence Success')
