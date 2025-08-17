import pandas as pd

data = {
    "Name": ["navya", "ram", "sujal", "kon", "navya", "ram", "sujal", "kon"],
    "Age": [20, 30 , 40, 50 ,10, 30 , 40, 50 ],
    "Salary": [1000, 2000, 3000 , 4000,1000, 2000, 3000 , 4000],
    "Perfomance Score": [ 85, 95 , 100 , 45 , 34 , 23, 67,79]

}


df = pd.DataFrame(data)
print("sample dataframe: ")
print(df)

print("descriptive stastics: ")
print(df.describe())