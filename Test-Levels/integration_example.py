import unittest
from simple_add import add
from simple_multiple import multiply


def compute(a, b):
    return multiply(a, add(a, b))


class TestCompute(unittest.TestCase):
    def test_compute_positive(self):
        result = compute(2, 3)
        self.assertEqual(result, 10)

    def test_compute_negative(self):
        result = compute(-2, -3)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
