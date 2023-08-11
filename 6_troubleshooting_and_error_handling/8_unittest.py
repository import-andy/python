'''unittest - unit testing framework

Allows to isolate & test functions'''

import unittest

a = 3
b = 5

# Defining 3 methods/functions inside a class:
class Testing(unittest.TestCase):

    def test_string(self):                # Methods within unittest should start with a STRING 'test'
        x = 'alpha'
        y = 'alpha'
        self.assertEqual(x, y)
    
    def test_equal(self):                
        self.assertEqual(3 + 4, a + b)

    def test_greater(self):
        self.assertTrue(a + b > 3 + 4)   # If we would change '>' to '<', then this methom would also be wrong

if __name__ == '__main__':
    unittest.main()

# Can see that 3 tests were run: 'F..' = failure, success, success - 3 total
# Tests always done in alphabetic order
# One (second) method is wrong, first and third are correct (because nothing is returned from that)
# Always make sure that all three functions are completely independent of each other

# Can run from Command Line with with more detail (higher verbosity):
# python 8_unittest.py -v
