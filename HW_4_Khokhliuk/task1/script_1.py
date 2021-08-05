

class Mammals():

    def __init__(self, name, is_predator, food_type, continent, age_of_living):
        self.name = name
        self.is_predator = is_predator
        self.food_type = food_type
        self.continent = continent
        self.age_of_living = age_of_living

    def eat(self):
        print(self.name, "is Eating")

    def talk(self):
        print(self.name, "is Talking")

    def breath(self):
        print(self.name, "is Breathing")

    def run(self):
        print(self.name, "is Running")

    def sleep(self):
        print(self.name, "is Sleeping")





my_mammal = Mammals(name="Tiger", is_predator=True, food_type="Meat", continent=["Africa", "Asia", "America"], age_of_living=13)

print(my_mammal.name)
print(my_mammal.is_predator)
print(my_mammal.continent)
print(my_mammal.food_type)
print(my_mammal.age_of_living)

my_mammal.sleep()
my_mammal.eat()
my_mammal.breath()
my_mammal.talk()
my_mammal.run()



