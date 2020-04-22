import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEquals('foo'.upper(), 'FOO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())

    def test_even(self):
        for i in range(0, 6):
           self.assertEqual(i % 2, 0)


