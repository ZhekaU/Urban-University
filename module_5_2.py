class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)
    def __str__(self):
        return (f'Название: {self.name} ,кол-во этажей: {self.number_of_floors}')

    def __len__(self):
        return self.number_of_floors

ph1 = House('ЖК Грани', 30)
ph2 = House('Коттеджный поселок Гармония', 4)
# ph1.go_to(3)
# ph2.go_to(5)
print(ph1)
print(ph2)
print(len(ph1))
print(len(ph2))
