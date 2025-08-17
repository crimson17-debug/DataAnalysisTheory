import pandas as pd

data = {
    "name": ['Ram', 'Shyam', 'Ghan'],
    "age": [10 , 20 , 30],
    "city": ['nagpur', 'himachal', 'kurnool']
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index = False)

# df.to_excel("output2.xlsx" , index=False)

df.to_json("output.json", index='False')