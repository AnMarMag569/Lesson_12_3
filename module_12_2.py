import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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

class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True
    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_usain_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        last_place_runner = list(results.values())[-1]
        self.assertEqual(last_place_runner, self.nik)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_andrey_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        last_place_runner = list(results.values())[-1]
        self.assertEqual(last_place_runner, self.nik)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_all_runners(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        last_place_runner = list(results.values())[-1]
        self.assertEqual(last_place_runner, self.nik)

#    @classmethod
#    def tearDownClass(cls):
#        for place, runner in cls.all_results.items():
#           print(f"{place}. {runner}")

if __name__ == '__main__':
   unittest.main()