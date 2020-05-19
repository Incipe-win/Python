class Pseudo:
    def __init__(self, name):
        self.name = name
        self.__age = 20

    def __function(self):
        print("%s is a %d handsome boy!" % (self.name, self.__age))


pseudo = Pseudo("RI")

print(pseudo._Pseudo__age)

pseudo._Pseudo__function()