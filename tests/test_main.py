import unittest
import os
from src.main import get_name

class TestMain(unittest.TestCase):
    def test_name(self):
        name = "Johns"
        expected = "Hello Johns"
        print(os.getenv("MODE"))
        self.assertEqual(get_name(name), expected)

if __name__ == "__main__":
    unittest.main()
