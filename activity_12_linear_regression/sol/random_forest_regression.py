# CS390Z - Introduction to Data Minining - Fall 2021
# Instructor: Thyago Mota
# Description: non-linear regression (attempt)

from google.colab import drive
import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# definitions/parameters
DATA_FOLDER = '/content/drive/MyDrive/Colab Datasets/country_indicators/'
DATASET_NAME = 'country_indicators.csv'

# Google drive mount
drive.mount('/content/drive')

# because this code will be executed after the linear regression, you can re-use the data frame defined previously

# TODO: try a non-linear regression using the random forest model, also displaying the obtained r2 score
model = RandomForestRegressor().fit(X, Y)
score = model.score(X, Y)
print('r2 score: {:.2f}'.format(score))

# TODO: produce a visualization of the data points and the fitted points
plt.scatter(X, Y)
Y_pred = model.predict(X)
plt.scatter(X, Y_pred, c=['red'])
plt.xlabel('GDP per capita')
plt.ylabel('Life Expectancy')
plt.show()
