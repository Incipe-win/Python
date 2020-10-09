import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import font_manager

my_font = font_manager.FontProperties(
    fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")


class Draw:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def run(self):
        plt.figure(figsize=(20, 15), dpi=80)
        plt.title("2010~2015年PM2.5变化情况", fontproperties=my_font)
        plt.xlabel("时间", fontproperties=my_font)
        plt.ylabel("PM2.5 变化", fontproperties=my_font)
        for area, data in self.data_dict.items():
            _x = data.index
            _y = data.values
            plt.plot(range(len(_x)), _y, label=area)
            plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)
        plt.legend(prop=my_font)
        plt.grid()
        plt.show()


class Handle:
    def run(self, file_path):
        data = pd.read_csv(file_path)
        data_time = pd.PeriodIndex(year=data["year"], month=data["month"],
                                   day=data["day"], hour=data["hour"], freq="H")
        data["datetime"] = data_time
        data.set_index("datetime", inplace=True)
        data = data.resample("7D").mean()
        return data["PM_US Post"]


if __name__ == "__main__":
    h = Handle()
    data_dict = dict()
    data_dict["北京"] = h.run("./PM2.5/BeijingPM20100101_20151231.csv")
    data_dict["成都"] = h.run("./PM2.5/ChengduPM20100101_20151231.csv")
    data_dict["广州"] = h.run("./PM2.5/GuangzhouPM20100101_20151231.csv")
    data_dict["上海"] = h.run("./PM2.5/ShanghaiPM20100101_20151231.csv")
    data_dict["沈阳"] = h.run("./PM2.5/ShenyangPM20100101_20151231.csv")

    d = Draw(data_dict)
    d.run()
