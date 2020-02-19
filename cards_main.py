#! /usr/bin/python3

import cards_tools

while True:

    cards_tools.show_menu()
    choose = input("请输入您的选择:")

    if choose in ["1", "2", "3"]:
        #  1. 新增名片
        if choose == "1":
            print("您的选择是: %s" % cards_tools.action[int(choose)])
            cards_tools.new_card()
        # 2. 显示全部
        elif choose == "2":
            print("您的选择是: %s" % cards_tools.action[int(choose)])
            cards_tools.show_all()
        # 3. 查询名片
        elif choose == "3":
            print("您的选择是: %s" % cards_tools.action[int(choose)])
            cards_tools.search_card()
    elif choose == "0":
        print("您的选择是: %s" % cards_tools.action[int(choose)])
        print("欢迎您的使用，祝您生活愉快！")
        break
    else:
        print("输入错误，请重新输入！", end="\n\n")
        continue
