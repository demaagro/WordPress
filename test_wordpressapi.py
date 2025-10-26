# test_wordpressapi.py
"""
Tests for WordPressAPI module.
"""

import unittest
from wordpressapi import WordPressAPI

class TestWordPressAPI(unittest.TestCase):
    """Test cases for WordPressAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WordPressAPI()
        self.assertIsInstance(instance, WordPressAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WordPressAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
