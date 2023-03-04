import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_tc_001_positive_add(self):
        result = add(1, 2)
        self.assertEquals(result, 3)

    def test_tc_002_negative_add(self):
        result = add(-1, -2)
        self.assertEquals(result, -3)

    def test_tc_003_float_add(self):
        result = add(-1.50, 20.50)
        self.assertEquals(result, 19.0)


if __name__ == "__main__":
    unittest.main()

