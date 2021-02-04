import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10.5, 5.5), 16)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(1.1, 1.5), 2.6)
    
    def test_sub(self):
        self.assertEqual(calc.sub(10.5, 5.5), 5)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(10, 1.5), 8.5)
        
    def test_mult(self):
        self.assertEqual(calc.mult(10.2, 4.2), 42.839999999999996)
        self.assertEqual(calc.mult(-1, 1), -1)
        self.assertEqual(calc.mult(1.1, 1.5), 1.6500000000000001)
        self.assertEqual(calc.mult(0, 1.5), 0)
        
    def test_div(self):
        self.assertEqual(calc.div(5, 2), 2.5)
        self.assertEqual(calc.div(-1, 1), -1)
        self.assertEqual(calc.div(-1, -1), 1)
        
        with self.assertRaises(ValueError):
            calc.div(10,0)
        
        
if __name__ == '__main__':
    unittest.main()