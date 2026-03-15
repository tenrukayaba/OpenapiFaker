# test_openapifaker.py
"""
Tests for OpenapiFaker module.
"""

import unittest
from openapifaker import OpenapiFaker

class TestOpenapiFaker(unittest.TestCase):
    """Test cases for OpenapiFaker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OpenapiFaker()
        self.assertIsInstance(instance, OpenapiFaker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OpenapiFaker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
