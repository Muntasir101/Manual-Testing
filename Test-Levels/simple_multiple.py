import unittest


def multiply(a, b):
    return a * b


class TestAdd(unittest.TestCase):
    def test_tc_001_positive_multiply(self):
        result = multiply(1, 2)
        self.assertEquals(result, 2)

    def test_tc_002_negative_multiply(self):
        result = multiply(-1, -2)
        self.assertEquals(result, 2)

    def test_tc_003_float_add(self):
        result = multiply(-1.50, 20.50)
        self.assertEquals(result, -30.75)


if __name__ == "__main__":
    unittest.main()

