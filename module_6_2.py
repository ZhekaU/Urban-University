class Vehicle:
    __COLOR_VARIANTS = ['Красный', 'Синий', 'Фиолетовый', 'Желтый', 'Черный', 'Белый']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color


    def repaint(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
            print(new_color)
        else:
            print(new_color,self.__COLOR_VARIANTS)

    def __str__(self):
        return f"{self.__model},{self.owner},{self.__engine_power},{self.__color})"

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

    def __str__(self):
        return f"{self.get_model()},{self.owner},{self.get_horsepower()},{self.get_color()},{self.__PASSENGERS_LIMIT})"

# Создаем объекты
vehicle = Vehicle("Иван", "Tesla Model S", 1000, "Красный")
sedan = Sedan("Мария", "BMW 3 Series", 180, "Синий")

# Вывод информации об объектах
print(vehicle)
print(sedan)


# Изменение цвета автомобиля
vehicle.repaint("Зеленый")  # Недопустимый цвет
print(vehicle)
vehicle.repaint("Черный")  # Допустимый цвет
print(vehicle)
