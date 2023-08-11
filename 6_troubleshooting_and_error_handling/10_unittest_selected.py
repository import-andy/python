"""unittest - selecting specifec tests to run"""

"""
1. So far, we have been using this command:
python 8_unittest.py -v

2. Now we will use this one - it will do the same thing:
python -m unittest 10_unittest_selected.py -v

3. But if we want to SELECT tests to be done - we can use this command:
python -m unittest -q 10_unittest_selected.TestArea.test_square -v

'-q' for quiet mode to resuce output size in console

4. Multiple selected tests:
python -m unittest -q 10_unittest_selected.TestArea.test_square 10_unittest_selected.TestArea.test_rectangle -v
"""

import unittest
import shape_area

class TestArea(unittest.TestCase):
    
    def test_triangle(self):
        self.assertEqual(shape_area.triangle(10, 5), 25)

    def test_rectangle(self):
        self.assertEqual(shape_area.rectangle(10, 10), 100) 

    def test_square(self):
        self.assertEqual(shape_area.square(2), 4)
    
if __name__ == '__main__':
    unittest.main()

