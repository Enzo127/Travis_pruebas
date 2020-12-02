import unittest
#import sys
#print(sys.path)
import Calculo


class Test_Engine(unittest.TestCase):
    def test_suma(self):
        result = Calculo.suma(3,5)
        self.assertEqual(result, 8)

    def test_resta(self):
        result = Calculo.resta(-6,5)
        self.assertEqual(result, -11)

    def test_mult(self):
        result = Calculo.mult(3,7)
        self.assertEqual(result, 21)


if __name__ == "__main__":
    unittest.main()
