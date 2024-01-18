import unittest
import fact
class testfact(unittest.TestCase):
    def test_zero(self):
        result=fact.factorial(0)
        self.assertEqual(result,1)
    
    def test_one(self):
        result=fact.factorial(1)
        self.assertEqual(result,1)
    
    def test_positive(self):
        result=fact.factorial(5)
        self.assertEqual(result,120)
    
    def test_negative(self):
        # alternate //self.assertRaises(ValueError,fact.factorial,-5)
        with self.assertRaises(ValueError):
            fact.factorial(-5)

if __name__=='__main__':
    unittest.main()
