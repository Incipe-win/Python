from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(
    fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")


# x = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归",
#      "生化危机6：终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]
# y = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28,
#      11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]
#
# plt.figure(figsize=(100, 100), dpi=80)
#
# plt.bar(range(len(x)), y, width=0.3)
#
# plt.xticks(ticks=range(len(x)), labels=x, fontproperties=my_font, rotation=45)
# plt.show()

a = ["xxx: xxx", "xxx", "xxx: xxxx", "xxx"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_width = 0.2

x_16 = list(range(len(a)))
x_15 = [i + bar_width for i in x_16]
x_14 = [i + bar_width for i in x_15]

plt.figure(figsize=(20, 15), dpi=80)
# plt.bar(x_16, b_16, width=bar_width, color="red", label="9月16日")
# plt.bar(x_15, b_15, width=bar_width, color="green", label="9月15日")
# plt.bar(x_14, b_14, width=bar_width, color="blue", label="9月14日")
plt.barh(x_16, b_16, height=bar_width, color="red", label="9月16日")
plt.barh(x_15, b_15, height=bar_width, color="green", label="9月15日")
plt.barh(x_14, b_14, height=bar_width, color="blue", label="9月14日")
plt.legend(prop=my_font)
plt.yticks(ticks=x_15, labels=a, fontproperties=my_font)

# plt.show()
plt.savefig("./bar.svg")
