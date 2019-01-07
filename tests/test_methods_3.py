#!/usr/bin/python
import unittest
from App.methods import comp


class TestCharts(unittest.TestCase):

    def setUp(self):
        pass

    def test_comp(self):
        # Get the output of nucleotide genbank file
        nucl_x_output, nucl_y_output = comp("6273289", "gb", "Nucleotide")
        # Test that both outputs are lists
        self.assertEqual(type(nucl_x_output), list)
        self.assertEqual(type(nucl_y_output), list)
        # Test that the output lists are of equal length
        self.assertEqual(len(nucl_x_output), len(nucl_y_output))
        # Get the output of protein genprot file
        prot_x_output, prot_y_output = comp("AAA29796.1", "gp", "Protein")
        # Test that both outputs are lists
        self.assertEqual(type(prot_x_output), list)
        self.assertEqual(type(prot_y_output), list)
        # Test that the output lists are of equal length
        self.assertEqual(len(prot_x_output), len(prot_y_output))


if __name__ == '__main__':
    unittest.main()
