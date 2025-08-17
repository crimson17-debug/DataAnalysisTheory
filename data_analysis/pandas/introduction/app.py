import pandas as pd

#read data from csv
# df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\data_analysis\pandas\sales_data_sample.csv', encoding="latin1")
# df = pd.read_excel(r'C:\Users\HP\OneDrive\Desktop\data_analysis\pandas\SampleSuperstore.xlsx')
df = pd.read_json(r'C:\Users\HP\OneDrive\Desktop\data_analysis\pandas\sample_Data.json')



print(df)