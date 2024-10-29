from datetime import datetime
import unittest
import os
from main import save_calcs, Saved

class TestSaveCalcs(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_results"
        self.results = [Saved(x=1.0, e=1e-6, fxe=0.64805379358818382407, N=6)]

    def test_save_calcs(self):
        # Ensure the file is saved correctly
        save_calcs(self.test_filename, self.results)
        self.assertTrue(os.path.isfile(self.test_filename + ".txt"))

        # Check content
        with open(self.test_filename + ".txt", 'r', encoding='utf-8') as f:
            content = f.read()

            self.assertIn("0.648053793588", content)



if __name__ == '__main__':
    unittest.main()