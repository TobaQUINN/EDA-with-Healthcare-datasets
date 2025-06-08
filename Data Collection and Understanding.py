# Data Collection and Understanding

import pandas as pd

df= pd.read_csv(r'C:\Users\DARA2\Documents\Healthcare Datasets.txt')
print(df.head())
print(df.describe(include='all'))
print(df.info())
print(df.columns)
print(df.shape)
print(df.isnull().sum())

