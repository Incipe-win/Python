from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

file_path = "./books.csv"

df = pd.read_csv(file_path)

print(df["original_publication_year"].sort_values())

# print(df.info())
# print(df.head(1))
# print(pd.notnull(df["original_publication_year"]))
# df = df[pd.notnull(df["original_publication_year"])]
# print(df)

# years = df.groupby(by="original_publication_year")
# print(years.count()["title"])
