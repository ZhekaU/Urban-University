import unittest
from Runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Oleg')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner_1 = Runner('Egor')
        for _ in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    def test_challenge(self):
        runner_2 = Runner('Ivan')
        runner_3 = Runner('Danil')
        for _ in range(10):
            runner_2.run()
            runner_3.walk()
        self.assertNotEqual(runner_2.distance, runner_3.distance)

    if __name__ == '__main__':
        unittest.main()
