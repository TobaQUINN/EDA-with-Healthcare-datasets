#Data Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os as os

df= pd.read_csv(r'C:\Users\DARA2\Documents\Cleaned_Healthcare_Datasets.csv')
# Creating directory for saving plots
os.makedirs('plots', exist_ok=True)
#setting style of seaborn
sns.set_style(style='darkgrid')

#For Age Distribution
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution of Patients')
#saving plot
plt.savefig('plots/age_distribution.png', dpi=300, bbox_inches='tight')
plt.show()



# Count plot for genders
sns.countplot(data=df, x='Gender')
plt.title('Gender Distribution of Patients')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(True)
# saving plot
plt.savefig('plots/count plot for gender distribution.png', dpi=300, bbox_inches='tight')
plt.show() ## from the plot,both the variables have the same frequency


#count plot for conditions
sns.countplot(data=df, x='Medical Condition')
plt.title('Medical Condition Distribution of Patients')
plt.xlabel('Medical Condition')
plt.ylabel('Count')
plt.grid(True)
#saving plot
plt.savefig('plots/count plot for medical condition distribution of patients.png')
plt.show() ## from the plot, most of the patients have arthritis and hypertension


#Box plot for Age vs Medical Condition
sns.boxplot(data=df, x='Medical Condition', y='Age')
plt.title('Age vs Medical Condition')
plt.xlabel('Medical Condition')
plt.ylabel('Age')
plt.grid(True)
#saving plot
plt.savefig('plots/box plot for age vs medical condition.png', dpi=300, bbox_inches='tight')
plt.show() ## from the plot, most of the patients with diabetes and hypertension are in the age group of 40-60 years 

# Bar chart for Admission Type Distribution
admission_type_counts = df['Admission Type'].value_counts()
sns.barplot(x=admission_type_counts.index, y=admission_type_counts.values, palette='viridis')
plt.title('Admission Type Distribution of Patients')
plt.xlabel('Admission Type')
plt.ylabel('Count')
plt.grid(True)
# saving plot
plt.savefig('plots/admission_type_distribution.png', dpi=300, bbox_inches='tight')
plt.show()  ## Elective Admission type is the most common type

# Count plot for Insurance Provider Distribution
sns.countplot(data=df, x='Insurance Provider', order=df['Insurance Provider'].value_counts().index)
plt.title('Insurance Provider Distribution of Patients')
plt.xlabel('Insurance Provider')
plt.ylabel('Count')
plt.grid(True)
# saving plot
plt.savefig('plots/insurance_provider_distribution.png', dpi=300, bbox_inches='tight')
plt.show()  ## from the plot, most of the patients are insured by Cigna


# Pie chart for Blood Type Distribution
blood_type_counts = df['Blood Type'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(blood_type_counts, labels=blood_type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Blood Type Distribution of Patients')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
# saving plot
plt.savefig('plots/blood_type_distribution.png', dpi=300, bbox_inches='tight')
plt.show()  ## from the plot, most of the patients have blood type AB+ and 12.3% of the patients have blood type O-
