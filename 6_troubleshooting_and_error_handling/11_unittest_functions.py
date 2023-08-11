"""unittest assert functions"""

import unittest
import rectangle_perimeter

# 1
class TruthTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)         # 'True' can be replaced with '(5 - 2) == 3'

    def test_assert_false(self):
        self.assertFalse(False)       # 'False' can be replaced with '(5 - 2) == 4'
# 2
class EqualityTest(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(6, 8-2)        

    def test_not_equal(self):
        self.assertNotEqual(7, 4*2)      
# 3
class TestArea(unittest.TestCase):

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter.get_perimeter(2, 3), 10)
    
    def test_error(self):
        self.assertRaises(
            ValueError,
            rectangle_perimeter.get_perimeter, 10, 0)   # 10 and 0 passed to assertRaises, not 'get.perimeter(10, 0)'

if __name__ == '__main__':
    unittest.main()