import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Дополнен атрибутом is_frozen

    @staticmethod
    def check_frozen(func):
        def wrapper(*args, **kwargs):
            instance = args[0]
            if not instance.is_frozen:
                return func(*args, **kwargs)
            else:
                print(f'Тесты в этом кейсе заморожены')
        return wrapper

    @check_frozen
    def test_walk(self):
        try:
            runner = Runner('Example', speed=-5)
            runner.walk()
            self.assertEqual(runner.distance, -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    @check_frozen
    def test_run(self):
        try:
            runner = Runner(123, speed=5)  # Передача неверного типа в name
            runner.run()
            self.assertEqual(runner.distance, 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')

if __name__ == "__main__":
    class EnhancedRunnerTest(RunnerTest):

        new_attribute = "example"

        def new_method(self):
            print("This is a new method")


    tests_1 = unittest.TestSuite()
    tests_1.addTest(unittest.TestLoader().loadTestsFromTestCase(EnhancedRunnerTest))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests_1)
