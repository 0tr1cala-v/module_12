import logging
import unittest
import rt_with_exceptions as rt


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner1 = rt.Runner(name='Пешеход', speed=-100)
            for _ in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info('Тест "test_walk" выполнен успешно')
        except ValueError:
            logging.warning(msg='Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner2 = rt.Runner(name=10, speed=10)
            for _ in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner3 = rt.Runner('Ещё один пешеход')
        runner4 = rt.Runner('Ещё один бегун')
        for _ in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)


if __name__ == '__main__':
    #logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
    #                    format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()