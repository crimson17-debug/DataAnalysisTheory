import pandas as pd

data = {
    "Name": ["navya", "ram", "sujal", "kon", "navya", "ram", "sujal", "kon"],
    "Age": [20, 30 , 40, 50 ,10, 30 , 40, 50 ],
    "Salary": [1000, 2000, 3000 , 4000,1000, 2000, 3000 , 4000],
    "Perfomance Score": [ 85, 95 , 100 , 45 , 34 , 23, 67,79]

}


df = pd.DataFrame(data)

# print("sample dataframe")
# print(df)

# print("/nsingle column: ")
# name = df["Name"]
# print(name)

# print("multiple columns: ")
# subset = df[["Name" , "Salary"]]
# print(subset)


# high_salary = df[df["Salary"] > 2000]
# print(high_salary)

comined_salary = df[(df["Salary"] > 2000) & (df["Age"] < 50)]
filtered_data = df[(df["Salary"] > 3000) + (df["Age"] > 30)]

print(comined_salary)
print(filtered_data)