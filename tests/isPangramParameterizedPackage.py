import unittest
from sample.isPangram import *
from parameterized import parameterized, parameterized_class

class isPangramParameterizedPackage(unittest.TestCase):
    def setUp(self):
        self.tmp = isPangram()

    @parameterized.expand([
        ("allletters","abcdefghijklmnopqrstuvwxyz", "True"),
        ("abc","abc", "False"),
        ("notall","dobrzezewtejtibiijestopcjaignore", "False"),
    ])
    def test_one_parameterized(self, testName, word, expected):
        self.assertEqual(self.tmp.game(word), expected)

    @parameterized.expand([
        ("number" ,43),
    ])

    def test_exception(self, exceptionName, word):
        with self.assertRaises(Exception):
            self.tmp.check(word)

    @parameterized_class(('testName','word', 'expected'), [
        ("allletters","abcdefghijklmnopqrstuvwxyz", "True"),
        ("abc","abc", "False"),
        ("notall","dobrzezewtejtibiijestopcjaignore", "False"),
    ])
    class FizzBuzzParameterizedPackage2(unittest.TestCase):
        def setUp(self):
            self.tmp = isPangram()

        def test_second_parameterized(self):
            self.assertEqual(self.tmp.game(self.word), self.expected)

    def tearDown(self):
        self.temp = None



if __name__ == '__main__':
    unittest.main()
