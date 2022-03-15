import unittest
from dictionary_update import average_scores

class myTestCase(unittest.TestCase):

    def test_average(self):
        self.score_dict = {"Test 1": 89, "Test 2": 76, "Test 3": 97}
        expected = 87.3333333
        actual = average_scores(self.score_dict)

        self.assertAlmostEqual(expected, actual)
    
    def test_average_five(self):
        self.score_dict = {"Test 1": 34, "Test 2": 50, "Test 3": 87, "Test 4": 45, "Test 5": 90}
        expected = 61.2
        actual = average_scores(self.score_dict)

        self.assertAlmostEqual(expected, actual)

    def test_average_zero(self):
        self.score_dict = {}
        expected = None
        actual = average_scores(self.score_dict)

        with self.assertRaises(ValueError):
            average_scores(self.score_dict)

if __name__ == '__main__':
    unittest.main()