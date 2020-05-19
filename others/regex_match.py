import re

names = ["name1", "_name", "2_name", "__name__"]

for i in names:
    ret = re.match("[a-zA-Z_]+[\w]*", i)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s 非法" % i)