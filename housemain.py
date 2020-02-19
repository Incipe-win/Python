import house
import houseitem

# 1. 创建家具
bed = houseitem.HouseItem("席梦思", 40)
chest = houseitem.HouseItem("衣柜", 2)
table = houseitem.HouseItem("餐桌", 20)

print(bed)
print(chest)
print(table)

# 2. 创建房子对象
my_home = house.House("两室一厅", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
