from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

my_font = font_manager.FontProperties(
    fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

# import matplotlib
#
# font = {"family": "Noto Sans Mono",
#         "weight": "bold",
#         "size": "larger"
#         }
# matplotlib.rc("font", **font)

# x = range(2, 26, 2)
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
#
# plt.figure(num="hh", figsize=(20, 8), dpi=80)
# plt.tick_params(axis='x', colors="green")
# x_ticks = [i/2 for i in range(4, 49)]
# x_labels = ["h" + str(i) for i in range(1, 14)]
# plt.xticks(x_ticks[::3], x_labels)
# plt.yticks(range(min(y), max(y) + 1))
#
# plt.plot(x, y)
# plt.savefig("./test.svg")
# plt.show()

# y = [random.randint(20, 35) for i in range(120)]
# cnt = 10
# x = []
# for i in range(120):
#     if i == 60:
#         cnt += 1
#     i %= 60
#     s = str(i) if i >= 10 else "0" + str(i)
#     x.append(str(cnt) + ":" + s)
# plt.figure(figsize=(100, 15), dpi=80)
# plt.tick_params(axis='both', colors="green")
# plt.xticks(list(range(120))[::3], labels=x[::3], rotation=45,
#            fontproperties=my_font)
# plt.yticks(range(19, 36))
# plt.xlabel("时间", fontproperties=my_font)
# plt.ylabel("温度 单位(摄氏度)", fontproperties=my_font)
# plt.title("10～12点每分钟气温变化情况", fontproperties=my_font)
# plt.plot(x, y)
# plt.show()


y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
x = ["{}岁".format(i) for i in range(11, 31)]

plt.figure(figsize=(20, 15), dpi=80)
plt.tick_params(axis="both", colors="green")
plt.xticks(list(range(20)), labels=x, rotation=45, fontproperties=my_font)
plt.yticks(range(min(y1), max(y1)))
plt.xlabel("xx", fontproperties=my_font)
plt.ylabel("xxxx 单位(个)", fontproperties=my_font)
plt.title("xx～xxxx", fontproperties=my_font)
plt.grid(alpha=0.4)
plt.plot(x, y1, color="green", label="xx")
plt.plot(x, y2, color="blue", label="xx")
plt.legend(prop=my_font)
# plt.show()
plt.savefig("./plot.svg")
