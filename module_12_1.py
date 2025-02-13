import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False
    def test_walk(self):
        runner = Runner("Коля")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Расстояние после 10 прогулок должно быть 50")

    def test_run(self):
        runner = Runner("Наташа")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Расстояние после 10 забегов должно быть 100")

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("Коля")
        runner2 = Runner("Наташа")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance, "Дистанции для бегунов должны быть разными")

if __name__ == '__main__':
    unittest.main()