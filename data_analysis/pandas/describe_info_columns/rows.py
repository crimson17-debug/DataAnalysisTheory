import pandas as pd

df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\data_analysis\pandas\sales_data_sample.csv', encoding = "latin1")

# print("display the 5 rows")
# print(df.head())


# print("display last 5 rows")
# print(df.tail())


print("display info: ")
print(df.info())