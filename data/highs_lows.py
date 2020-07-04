import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    for row in reader:
        # print(row[1])
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except:
            print(current_date, "missing date")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # print(len(highs))
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.title("Daily high and low temperatures - 2014\nDeath Vally, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
