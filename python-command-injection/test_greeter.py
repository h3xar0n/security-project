import unittest
from unittest.mock import patch
import os
from greeter import Greeter

class TestGreeter(unittest.TestCase):

    def test_greet_happy_path(self):
        # Create a dummy file for ls to find
        dummy_file_path = "test_file.txt"
        with open(dummy_file_path, "w") as f:
            f.write("hello")

        # Patch os.system to prevent actual command execution during the test
        with patch('os.system') as mock_os_system:
            greeter = Greeter()
            greeter.greet(dummy_file_path)
            
            # Assert that os.system was called with the expected command
            mock_os_system.assert_called_once_with(f"ls {dummy_file_path}")

        # Clean up the dummy file
        os.remove(dummy_file_path)

if __name__ == "__main__":
    unittest.main()
