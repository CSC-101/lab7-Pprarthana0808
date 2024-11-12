
import unittest
from convert import str_to_float

class TestStrToFloat(unittest.TestCase):
    #test1
    def test_valid_float(self):
        self.assertEqual(str_to_float("3.14159"), 3.14159)
        self.assertEqual(str_to_float("123.45"), 123.45)
        self.assertEqual(str_to_float("-0.987"), -0.987)
        self.assertEqual(str_to_float("0.0"), 0.0)
    #test2
    def test_invalid_float(self):
        self.assertIsNone(str_to_float("hello"))
        self.assertIsNone(str_to_float("eta"))
        self.assertIsNone(str_to_float("1e"))
        self.assertIsNone(str_to_float(""))
    #test3
    def test_edgecases(self):
        self.assertIsNone(str_to_float(" "))
        self.assertEqual(str_to_float("-4.56e-3"), -0.00456)
        self.assertEqual(str_to_float("1e3"), 1000.0)
        self.assertEqual(str_to_float("-0.0"), -0.0)
if __name__ == "__main__":
    unittest.main()
