import unittest
from unittest.mock import patch, MagicMock
import os
from greeter import Greeter

class TestGreeter(unittest.TestCase):

    def test_greet_happy_path(self):
        # Create a dummy file for ls to find
        dummy_file_path = "test_file.txt"
        with open(dummy_file_path, "w") as f:
            f.write("hello")

        # Patch subprocess.run to prevent actual command execution during the test
        with patch('subprocess.run') as mock_subprocess_run:
            # Configure the mock to return a successful result
            mock_subprocess_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

            greeter = Greeter()
            greeter.greet(dummy_file_path)
            
            # Assert that subprocess.run was called with the expected command and arguments
            mock_subprocess_run.assert_called_once_with(["ls", dummy_file_path], check=True, capture_output=True, text=True)

        # Clean up the dummy file
        os.remove(dummy_file_path)

if __name__ == "__main__":
    unittest.main()
