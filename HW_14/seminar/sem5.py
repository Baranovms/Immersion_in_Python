from Rectangle import Rectangle
import unittest

class TestUnitCheck(unittest.TestCase):

    def setUp(self):
        self.first = Rectangle(2, 3)
        self.second = Rectangle(4, 5)

    def test_eq(self):
        self.assertTrue(self.first == self.first)

    def test_not_eq(self):
        self.assertFalse(self.first == self.second)

    def test_sum(self):
        self.assertEqual(self.first + self.second, Rectangle(6, 8))

    def test_exist(self):
        self.assertRaises(ValueError, Rectangle, (0, 3))

if __name__ == '__main__':
    unittest.main(verbosity=2)
