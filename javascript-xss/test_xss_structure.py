import unittest
import os

class TestXSSStructure(unittest.TestCase):

    def test_v_html_present_with_initial_content(self):
        html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')
        with open(html_file_path, 'r') as f:
            content = f.read()

        # Assert that the v-html directive is present with the initial content
        self.assertIn("v-html=\"userInput\"", content)
        self.assertIn("userInput: '<b>Hello from Vue!</b>'", content)

if __name__ == "__main__":
    unittest.main()

