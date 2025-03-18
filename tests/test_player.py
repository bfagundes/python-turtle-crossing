import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """"Set up the test environment before each test"""
        pass

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)