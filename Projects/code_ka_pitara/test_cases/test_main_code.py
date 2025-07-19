import unittest
from main_code import add

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        result = add(2,3)
        self.assertEqual(result,5)

    def test_add_positive(self):
        self.assertEqual(add(10, 5), 15)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == '__main__':
    unittest.main()