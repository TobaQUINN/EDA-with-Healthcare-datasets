#Data Cleaning and Preprocessing with descriptive statistics

import pandas as pd

df= pd.read_csv(r'C:\Users\DARA2\Documents\Healthcare Datasets.txt')
df.dropna(inplace=True)
df.duplicated().sum()
df.drop_duplicates(inplace=True)

print(df.tail())

#Renaming columns for domain understanding

data = {'Blood Type': [1, 2, 3], 'Blood Group': [4, 5, 6]}
df = pd.DataFrame(data)

# Rename columns
df.rename(columns={'Blood Type': 'Blood Group'}, inplace=True)

# Saving Dataset
df.to_csv('Cleaned_Healthcare_Datasets.csv', index=False)
print(df.head())
