"""
从控制台输入要出的拳 - 石头（1） / 剪刀（2） / 布（3）
电脑随机出拳
比较胜负
"""
import random
import multiple

player = int(input("请输入您要出的拳 石头（1） / 剪刀（2） / 布（3） : "))
computer = random.randint(1, 3)

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("player win!")
    print("computer is %d" % computer)
elif player == computer:
    print("nobody win!")
    print("computer is %d" % computer)
else:
    print("computer win!")
    print("computer is %d" % computer)

multiple.fun()
