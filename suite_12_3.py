import unittest
import tests_12_3

tests_1 = unittest.TestSuite()
tests_1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
tests_1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tests_1)

