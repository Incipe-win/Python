import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())
# for i, j in group:
#     print(type(i))
#     print("-" * 100)
#     print(j)
#     print("*" * 100)

# cn_data = df[df["Country"] == "CN"]
# cn_group = cn_data.groupby(by="State/Province")
# print(cn_group.count()["Brand"])
