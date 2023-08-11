"""unittest - skipping tets"""

import unittest
import rectangle_perimeter
import sys

class TestArea(unittest.TestCase):
   
    @unittest.skip('Temporarily skips error test')          # skipping this test
    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter.get_perimeter(2, 3), 10)
    
    @unittest.skipIf(sys.version_info[0] < 3,               # skipping if
                    'This test requires Python 3 or higher')
    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 0)

    @unittest.skipUnless(sys.platform.startswith('win'),    # skipping if not
                        'Requires Windows')
    def test_equal(self):
        self.assertTrue(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()