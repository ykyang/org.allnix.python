import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import org.allnix.util
import org.util
import org.allnix.lp.util

class TestPackage(unittest.TestCase):
    """Learn package path"""

    def test(self):
        self.assertEqual(org.util.read(), "org")
        self.assertEqual(org.allnix.util.read(), "org.allnix")
        self.assertEqual(org.allnix.lp.util.read(), "org.allnix")

