import pandas as pd

fields = ["mean", "std", "MET"]

df = pd.read_csv("statistics.csv")
df1 = df.loc[df["function"] == "michalewicz"]
df2 = df1.loc[df1["dimension"] == 30]

for field in fields:
    print(field)
    print(pd.Series.tolist(df2[field]))
