import unittest
from sample.isPangram import *

class isPangramParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/is_pangram_data_test")
      tmpIsPangram = isPangram()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            inp, result = (data[0]), data[1].strip("\n")
            self.assertEqual(tmpIsPangram.game(inp), result)
      fileTest.close()

    def test_from_file_exception(self):
        fileTest2 = open("data/is_pangram_data_exception")
        tmpIsPangram = isPangram()
        for line in fileTest2:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp, result = (data[0]), data[1].strip("\n")
                self.assertRaisesRegex(Exception, result, tmpIsPangram.game, inp)
        fileTest2.close()


if __name__ == '__main__':
    unittest.main()
