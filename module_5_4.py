class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def go_to(self, new_floor: int):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __str__(self):
        return (f'Название: {self.name} ,кол-во этажей: {self.number_of_floors}')

    def __len__(self):
        return self.number_of_floors


ph1 = House('ЖК Грани', 10)
print(House.houses_history)
ph2 = House('Коттеджный поселок Гармония', 20)
print(House.houses_history)
ph3 = House('ЖК Матрёшки двор', 20)
print(House.houses_history)

# Удаление объектов
del ph2
del ph3
# ph1.go_to(3)
# ph2.go_to(5)
# print(ph1)
# print(ph2)
# # print(len(ph1))
# # print(len(ph2))
# print(ph1 == ph2)  # __eq__
# print(ph1 < ph2)  # __lt__
# print(ph1 <= ph2)  # __le__
# print(ph1 > ph2)  # __gt__
# print(ph1 >= ph2)  # __ge__
# print(ph1 != ph2)  # __ne__
# ph1 = ph1 + 10  # __add__
# print(ph1)
# print(ph1 == ph2)
# ph1 += 10  # __iadd__
# print(ph1)
#
# ph2 = 10 + ph2  # __radd__
# print(ph2)
