## Age and Room number(numerical features) feature relation

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv(r'C:\Users\DARA2\Documents\Cleaned_Healthcare_Datasets.csv')

# Select numeric features
numeric_df = df.select_dtypes(include='number')
correlation = numeric_df.corr()

# Plotting the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", square=True, linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.tight_layout()
plt.show()

sns.pairplot(numeric_df, diag_kind='kde', corner=True)
plt.suptitle('Pairplot of Numerical Features', y=1.02)
plt.show()


