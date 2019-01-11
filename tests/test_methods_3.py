#!/usr/bin/python
import unittest
from App.methods import comp, skew


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
        # Get the output of nucleotide fasta file
        nucl2_x_output, nucl2_y_output = comp("EU490707", "fasta", "Nucleotide")
        # Test that both outputs are lists
        self.assertEqual(type(nucl2_x_output), list)
        self.assertEqual(type(nucl2_y_output), list)
        # Test that both output lists are of equal length
        self.assertEqual(len(nucl2_x_output), len(nucl2_y_output))
        # Get the output of protein genprot file
        prot_x_output, prot_y_output = comp("AAA29796.1", "gp", "Protein")
        # Test that both outputs are lists
        self.assertEqual(type(prot_x_output), list)
        self.assertEqual(type(prot_y_output), list)
        # Test that the output lists are of equal length
        self.assertEqual(len(prot_x_output), len(prot_y_output))
        # Get the output of protein fasta file
        prot2_x_output, prot2_y_output = comp("PKU88159.1", "fasta", "Protein")
        # Test that both outputs are lists
        self.assertEqual(type(prot2_x_output), list)
        self.assertEqual(type(prot2_y_output), list)
        # Test that the output lists are of equal length
        self.assertEqual(len(prot2_x_output), len(prot2_x_output))

    def test_skew(self):
        # Get output of nucleotide genbank file
        gen_x_output, gen_y_output = skew("6273289", "gb")
        # Test that both outputs are lists
        self.assertEqual(type(gen_x_output), list)
        self.assertEqual(type(gen_y_output), list)
        # Test that the lists are of equal length
        self.assertEqual(len(gen_x_output), len(gen_y_output))
        # Get the output of nucleotide fasta file
        fast_x_output, fast_y_output = skew("EU490707", "fasta")
        # Test that both outputs are lists
        self.assertEqual(type(fast_x_output), list)
        self.assertEqual(type(fast_y_output), list)
        # Test that the output lists are of equal length
        self.assertEqual(len(fast_x_output), len(fast_y_output))


if __name__ == '__main__':
    unittest.main()
