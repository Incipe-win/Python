import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

rating = df["Rating"].values

max_rating = max(rating)
min_rating = min(rating)

bins_list = [1.6]
bins_list = [1.6] + [0.5] * 10

plt.figure(figsize=(20, 15), dpi=80)

x_ticks = []
while i <= max_rating:
    i = i + 0.5
