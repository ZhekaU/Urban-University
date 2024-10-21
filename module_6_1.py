class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def __str__(self):
        return self.name,self.alive,self.fed

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                self.fed = True
                print(self.name,food.name)
            else:
                self.alive = False
                print(self.name,food.name)
        else:
            print(self.name,food)

class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                self.fed = True
                print(self.name,food.name)
            else:
                self.alive = False
                print(self.name,food.name)
        else:
            print(self.name,food)

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

    def __str__(self):
        return self.name,self.edible

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)

    def __str__(self):
        return self.name,self.edible

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)