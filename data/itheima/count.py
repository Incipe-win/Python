import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

temp_genre = df["Genre"].str.split(",").tolist()
genre = set([i for j in temp_genre for i in j])

rows = df.shape[0]
cols = len(genre)

arr = pd.DataFrame(np.zeros((rows, cols)), columns=genre)

for i in range(rows):
    arr.loc[i, temp_genre[i]] = 1
    # for j in temp_genre[i]:
    #     arr.loc[i, j] = 1

genre_count = arr.sum(axis=0)
genre_count = genre_count.sort_values()
plt.figure(figsize=(20, 15), dpi=80)
# x_ticks = range(len(genre_count.index))
plt.bar(genre_count.index, genre_count.values)
plt.show()
