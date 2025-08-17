import numpy as np
import pandas as pd

# loading the dataset

df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\data_analysis\indian_employee_dataset\Titanic-Dataset.csv')

# df = pd.read_csv('C:\Users\HP\OneDrive\Desktop\data_analysis\indian_employee_dataset\large_dataset_with_nulls.csv')
print(df.head())

# checking the missin values

print("missing values in each column:")
print(df.isnull().sum())

