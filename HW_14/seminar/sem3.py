import unittest
from sem1_2 import clear_text

class TestUniMy(unittest.TestCase):

    def setUp(self):
        self.correct = 'text'
        self.first = 'Te...xt'
        self.third = 'TeЯЯЯяяяяxt'
        self.forth = 'T..eЯ..ЯЯ.....яяя...яxt'

    def test_step_1(self):
        self.assertEqual(self.correct, clear_text(self.first))

    def test_step_2(self):
        self.assertTrue(self.correct == clear_text(self.second))

    def test_step_3(self):
        self.assertFalse(self.correct is clear_text(self.third))

    def test_step_4(self):
        self.assertRaises(ValueError, clear_text(None))

if __name__ == '__main__':
    unittest.main(verbosity=2)