def func(a, b, *argc, **argv):
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    print(argc)
    print(type(argc))
    print(argv)
    print(type(argv))
    print("*" * 20)
    print(*argc)
    return argv


# value1, value2 = func(1, 2, 3, 4, {1: 1, "2": "2"})
# print(type(func(1, 2, 3, 4, {1: 1, "2": "2"})))
# print(value1)
# print(value2)
ret = func(1, 2, 3, 4, {1: 1, "2": "2"}, x=1, y=2)
# ret = func(1, 2, 3, 4, {1: 1, "2": "2"})
print(ret)
