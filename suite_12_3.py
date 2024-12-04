import unittest
from module_12_1 import RunnerTest
from module_12_2 import TournamentTest


# Создание TestSuite
def create_test_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(RunnerTest)
    suite.addTest(loader.loadTestsFromTestCase(TournamentTest))
    return suite

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(create_test_suite())