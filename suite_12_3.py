import unittest
import tests_12_1 as t1
import tests_12_2 as t2

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(t1.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(t2.TournamentTest))

runner_ = unittest.TextTestRunner(verbosity=2)
runner_.run(suite)

