from calc import add, subtract, multiply, divide
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-4, -9), -13)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(3, -3), 6)
        self.assertEqual(subtract(-3, 3), -6)
        self.assertEqual(subtract(-3, -4), 1)

    def test_multiply(self):
        self.assertEqual(multiply(5, 4), 20)
        self.assertEqual(multiply(4, 0), 0)
        self.assertEqual(multiply(4, -5), -20)
        self.assertEqual(multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(6, -2), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()