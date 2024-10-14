import unittest
import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rt.Runner('Усэйн', 10)
        self.runner2 = rt.Runner('Андрей', 9)
        self.runner3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_t1(self):
        tournament1 = rt.Tournament(90, self.runner1, self.runner3)
        result = tournament1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament1'] = result

    def test_t2(self):
        tournament2 = rt.Tournament(90, self.runner2, self.runner3)
        result = tournament2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament2'] = result

    def test_t3(self):
        tournament3 = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament3'] = result

    def additional_test(self):
        """
            Данный тест выявляет ошибку метода start класса Tournament
            Ошибка заключается в том, что объект может быть удалён из списка participants
            до того, как выполнится весь цикл для каждого объекта
        """
        tournament4 = rt.Tournament(5, self.runner1, self.runner2, self.runner3)
        result = tournament4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament4'] = result

if __name__ == '__main__':
    unittest.main()