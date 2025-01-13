from Runner_new import Runner, Tournament
import unittest
from pprint import pprint

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner('Usain', speed=10)
        self.Andrey = Runner('Andrey', speed=9)
        self.Nick = Runner('Nick', speed=3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            formatted_result = {place: str(runner) for place, runner in result.items()}
            print(f'{test_name}: {formatted_result}')

    def test_Usain_and_Nick(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        results = tournament.start()
        self.__class__.all_results['test_Usain_and_Nick'] = results
        self.assertTrue(results[max(results.keys())] == self.Nick)

    def test_Andrey_and_Nick(self):
        tournament = Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()
        self.__class__.all_results['test_Andrey_and_Nick'] = results
        self.assertTrue(results[max(results.keys())] == self.Nick)

    def test_Usain_Andrey_and_Nick(self):
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()
        self.__class__.all_results['test_Usain_Andrey_and_Nick'] = results
        self.assertTrue(results[max(results.keys())] == self.Nick)

if __name__ == "__main__":
    unittest.main()
