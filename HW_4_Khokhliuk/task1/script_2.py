from script_1 import Mammals


class CatFamily(Mammals):

    def __init__(self):
        Mammals.__init__(self)
        pass


class Cat(CatFamily):

    def __init__(self):
        CatFamily.__init__(self)
        pass

    def talk():
        print("Meow!")


print(Cat.talk())
