from src.classmodule import Pinatas
import unittest

class TestCandiesValuesProcessing(unittest.TestCase):
    def test_empty_list(self):
        args = []
        pinatas = Pinatas()

        with self.assertRaises(ValueError):
            pinatas.candies = args

    def test_non_numeric_value(self):
        args = [2, '/', 'r']
        pinatas = Pinatas()

        with self.assertRaises(ValueError):
            pinatas.candies = args

    def test_zero_value(self):
        args = [2, 3, 1, 0, 5]
        pinatas = Pinatas()

        with self.assertRaises(ValueError):
            pinatas.candies = args

    def test_negative_value(self):
        args = [-2, 3, -1, 5]
        pinatas = Pinatas()

        with self.assertRaises(ValueError):
            pinatas.candies = args

    def test_type_value_transform(self):
        args = ['5', '4', '3', '2', '1']
        pinatas = Pinatas()
        pinatas.candies = args

        self.assert_(pinatas.candies, [5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
