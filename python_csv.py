import csv
import pandas as pd

data = {"Name": ["Ashit","amit","ankit","subham","sushree"], 
        "Age": [22, 20, 21, 21, 23]}

data = pd.DataFrame(data)
data.to_csv("age_data.csv", index=False)
print(data.head())

data = pd.read_csv("age_data.csv")
print(data.head())
