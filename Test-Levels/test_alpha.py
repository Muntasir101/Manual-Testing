import unittest


class AlphaTestCase(unittest.TestCase):
    def test_addition(self):
        result = 1 + 1
        self.assertEqual(result, 2)

    def test_subtraction(self):
        result = 1 - 1
        self.assertEqual(result, 0)

    def test_multiplication(self):
        result = 2 * 2
        self.assertEqual(result, 4)

    def test_division(self):
        result = 10 / 5
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
