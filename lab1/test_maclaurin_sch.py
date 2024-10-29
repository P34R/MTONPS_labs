import math
import unittest

import mpmath

from main import maclaurin_sch

class TestMaclaurinSch(unittest.TestCase):
    def test_maclaurin_sch(self):
        test_xs = [
            math.pi/4,
            math.pi/8,
            1,
            -1
        ]
        test_es = [
            0.0001,
            0.00001,
            0.000001
        ]
        for x in test_xs:
            expect = mpmath.sech(x)
            for e in test_es:
                our = maclaurin_sch(x,e)
                self.assertAlmostEqual(our[0],expect,places=3)


    def test_invalid_values(self):
        invalid_x_values = [ math.pi/2.0, -math.pi/2.0, math.pi]
        invalid_e_values = [0,1]

        e = 0.001
        for x in invalid_x_values:
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    maclaurin_sch(x, e)
        validX = 1.0
        for invalidE in invalid_e_values:
            with self.subTest(e=invalidE):
                with self.assertRaises(ValueError):
                    maclaurin_sch(validX,invalidE)
if __name__ == '__main__':
    unittest.main()