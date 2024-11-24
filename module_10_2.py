import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            if self.enemies > 0:
                print(f"{self.name} сражается {self.days} день(дня/дней)... осталось {self.enemies} воинов.")
            else:
                print(f"{self.name} одержал победу спустя {self.days} день(дня/дней)!")



knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight("Sir Galahad", 20)
knight3 = Knight("Сэр Персиваль", 10)

knight1.start()
knight2.start()
knight3.start()

knight1.join()
knight2.join()
knight3.join()
print('Все битвы закончились!')