class Cat:

    def __init__(self, new_name):
        print("相当于构造函数！(带参数)")
        self.name = new_name

    def eat(self):
        print("%s 爱吃！" % self.name)


tom_cat = Cat("Tom")
lazy_cat = Cat("LazyCat")
tom_cat.eat()
lazy_cat.eat()
