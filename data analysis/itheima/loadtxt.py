import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# us = np.loadtxt(us_file_path, delimiter=',', dtype="int")
uk = np.loadtxt(uk_file_path, delimiter=',', dtype="int")
uk = uk[uk[:, 1] <= 500000]

# us_comments = us[:, -1]
# us_comments = us_comments[us_comments <= 5000]

uk_comments = uk[:, -1]
uk_like = uk[:, 1]

# d = 5
# bin_nums = (np.max(us_comments) - np.min(us_comments)) // d
# plt.figure(figsize=(20, 8), dpi=80)
# plt.hist(us_comments, bin_nums)
# plt.show()
plt.figure(figsize=(20, 8), dpi=80)
plt.grid()
plt.scatter(uk_like, uk_comments)
plt.show()
