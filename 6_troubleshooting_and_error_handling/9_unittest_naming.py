"""Naming the test function

This is the correct way of testing
- source which needs to be tested is imported
- and their functions tested here, using different assert statements
"""

import unittest
import triangle_area        # importing our script

class TestArea(unittest.TestCase):

    def triangle_test(self):                          # Methods within unittest should start with a STRING 'test', not like here
        '''because of the name NOT starting with 'test' string, thhis will not be tested'''
        result = triangle_area.triangle(10, 5)        # passing height of 10 and a base of 5
        self.assertEqual(result, 25)

    def test_triangle(self):                          # Changed the name, so that it starts with 'test' string
        result = triangle_area.triangle(10, 5)    
        self.assertEqual(result, 25)

    def runTest(self):                                
        """the only name exception is 'runTest' name.
        But running this program will result into 1 test completed anyway.
        And if you comment the method above, it will still show only one method tested.
        Because they are the same thing, I believe."""
        result = triangle_area.triangle(10, 5)    
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()