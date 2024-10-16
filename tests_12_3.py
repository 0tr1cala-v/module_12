import unittest
import runner_and_tournament as rt
import runner


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = runner.Runner('Пешеход')
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = runner.Runner('Бегун')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner3 = runner.Runner('Ещё один пешеход')
        runner4 = runner.Runner('Ещё один бегун')
        for _ in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_t1(self):
        tournament1 = rt.Tournament(90, self.runner1, self.runner3)
        result = tournament1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament1'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_t2(self):
        tournament2 = rt.Tournament(90, self.runner2, self.runner3)
        result = tournament2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament2'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_t3(self):
        tournament3 = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник должен быть последним')
        self.all_results['test_tournament3'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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