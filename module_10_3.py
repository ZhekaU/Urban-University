import threading
from random import randint
import time

class Bank:
    def __init__(self, balance: int):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f'th1 Пополнение: {amount}. Баланс: {self.balance}')
                if self.balance >= 500 and not self.lock.locked():
                    pass
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            amount = randint(50, 500)
            print(f' Запрос на {amount}')
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'th2 Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
                    print(f'Итоговый баланс: {self.balance}')
                    self.lock.acquire()
            time.sleep(0.001)


bk = Bank(0)


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')