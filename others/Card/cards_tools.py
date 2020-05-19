action = ("0. 退出系统", "1. 新建名片", "2. 显示全部", "3. 查询名片")
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 62)
    print("欢迎使用【名片管理系统】v1.0".center(52))
    print("")
    print(action[1].center(55))
    print(action[2].center(55))
    print(action[3].center(55))
    print("")
    print(action[0].center(55))
    print("*" * 62)


def new_card():
    """新增名片"""
    name_str = input("1. 请输入姓名: ")
    telephone_str = input("2. 请输入电话: ")
    qq_str = input("3. 请输入QQ: ")
    email_str = input("4. 请输入email: ")

    card_dict = {"name": name_str,
                 "telephone": telephone_str,
                 "qq": qq_str,
                 "email": email_str}

    card_list.append(card_dict)

    print(card_list)
    print("添加 %s 的名片成功！" % name_str)


def show_all():
    """显示所有名片"""
    # 提示是否存在名片
    if len(card_list) == 0:
        print("没有名片建立，请先建立名片！")
        return
    # 打印表头
    for header in ["姓名", "电话", "QQ", "邮箱"]:
        print(header, end="\t\t\t\t")
    print("")

    # 打印分割线
    print("-" * 62)

    # 打印信息
    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card["name"],
                                        card["telephone"],
                                        card["qq"],
                                        card["email"]))
    print("")


def search_card():
    """搜索名片"""
    find_name = input("请输入要搜索的姓名: ")
    for card in card_list:
        if card["name"] == find_name:
            for header in ["姓名", "电话", "QQ", "邮箱"]:
                print(header, end="\t\t\t\t")
            print("")
            print("-" * 62)
            print("%s\t\t%s\t\t%s\t\t%s" % (card["name"],
                                            card["telephone"],
                                            card["qq"],
                                            card["email"]))

            # 修改删除操作
            deal_card(card)
            break
    else:
        print("没有找到 %s，请重新输入！" % find_name)


def deal_card(find_dict):
    """修改删除

    :param find_dict: 查找的字典
    :return:
    """
    while True:
        choose = input("请输入对这条名片的操作: [1]. 修改/ [2]. 删除/ [0]. 返回上级菜单")
        if choose in ["1", "2"]:
            if choose == "1":
                find_dict["name"] = input_card_info(find_dict["name"], "姓名: ")
                find_dict["telephone"] = input_card_info(find_dict["telephone"], "电话: ")
                find_dict["qq"] = input_card_info(find_dict["qq"], "QQ: ")
                find_dict["email"] = input_card_info(find_dict["email"], "邮箱: ")
            else:
                card_list.remove(find_dict)
                print("删除名片成功！")
            break
        elif choose == "0":
            return
        else:
            print("格式不正确，请重新输入！")
            continue


def input_card_info(dict_value, tip_message):
    """ 输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容返回输入内容，否则返回原有内容
    """
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
