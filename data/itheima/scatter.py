from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

my_font = font_manager.FontProperties(
    fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

y_3 = [random.randint(0, 30) for i in range(31)]
y_10 = [random.randint(0, 30) for i in range(31)]

x_3 = range(1, 32)
x_10 = range(51, 82)

plt.figure(figsize=(20, 15))

x = list(x_3) + list(x_10)
x_labels = ["3月{}日".format(i) for i in x_3]
x_labels += ["10月{}日".format(i - 50) for i in x_10]

plt.xticks(ticks=x[::2], labels=x_labels[::2], fontproperties=my_font,
           rotation=45)

plt.yticks(range(min(min(y_3), min(y_10)) - 1, max(max(y_3), max(y_10)) + 1))

plt.tick_params(axis="both", color="black")

plt.xlabel(xlabel="温度", fontproperties=my_font, color="blue")
plt.ylabel(ylabel="时间", fontproperties=my_font, color="green")
plt.title(label="3月和10月温度变化散点图", fontproperties=my_font, color="red")
# plt.grid(alpha=0.4)

plt.scatter(x_3, y_3, color="pink", label="3月", cmap=plt.cm.Blues)
plt.scatter(x_10, y_10, color="purple", label="10月", cmap=plt.cm.Blues)
plt.legend(prop=my_font)
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
# plt.show()
plt.savefig("./scatter.svg")
