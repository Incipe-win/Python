import numpy as np
from matplotlib import pyplot as plot

us_data = "./youtube_video_data/US_video_data_numbers.csv"
uk_data = "./youtube_video_data/GB_video_data_numbers.csv"

us_data = np.loadtxt(us_data, delimiter=",", dtype=int)
uk_data = np.loadtxt(uk_data, delimiter=",", dtype=int)

zeros_data = np.zeros((us_data.shape[0], 1)).astype(int)
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)

us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data, ones_data))

final_data = np.vstack((uk_data, us_data))
print(final_data)
