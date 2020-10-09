import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# f = pd.read_csv("./dogNames2.csv")
# print(f)
# print("*" * 100)
# print(f[(f["Row_Labels"].str.len() > 4) & (f["Count_AnimalName"] > 700)])
# print("*" * 100)
# print()

# file_path = "./IMDB-Movie-Data.csv"
# df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(1))
# print(df["Rating"].mean())
# print(len(set(df["Director"])))
# print(len(df["Director"].unique()))
# temp_actors_list = df["Actors"].str.split(", ").tolist()
# actors_list = [i for j in temp_actors_list for i in j]
# print(len(set(actors_list)))
# print(np.array(temp_actors_list))
# actors_list = np.array(temp_actors_list).flatten()
# print(actors_list)

file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
# rating = df["Rating"].tolist()
# runtime = df["Runtime (Minutes)"].tolist()
runtime = df["Runtime (Minutes)"].values
max_runtime = max(runtime)
min_runtime = min(runtime)

d = 5
bins = (max_runtime - min_runtime) // d

plt.figure(figsize=(20, 15), dpi=80)
plt.hist(runtime, bins)
plt.grid()
plt.xticks(range(min_runtime, max_runtime + d, d))
plt.show()
