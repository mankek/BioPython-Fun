#!/usr/bin/python
import unittest
from App.methods import retrieve, global_record, preview, upload, get_files
import os
import urllib.error


class TestNCBIOps(unittest.TestCase):

    # def setUp(self):
    #     # Make sure global record is empty
    #     global_record.clear()

    def test_retrieve(self):
        # Test retrieval of single nucleotide fasta file
        self.assertEqual(retrieve("nuccore", "EU490707", "fasta"), "done")
        # Test of retrieval of multiple genbank files
        self.assertEqual(retrieve("nuccore", "6273289,6273290,6273291", "gb"), "done")
        # Test of retrieval of single protein fasta file
        self.assertEqual(retrieve("protein", "PKU88159.1", "fasta"), "done")
        # Test of retrieval of multiple protein genprot files
        self.assertEqual(retrieve("protein", "AAA29796.1,PKU88155.1", "gp"), "done")
        # Test that retrieved files exist in correct location
        for i, h in zip(["EU490707", "6273289", "6273290", "6273291", "PKU88159.1", "AAA29796.1", "PKU88155.1"],
            ["fasta", "gb", "gb", "gb", "fasta", "gp", "gp"]):
            self.assertTrue(os.path.exists(os.path.join(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))), "App", "Files", i + "." + h)))
        # Test that retrieved files were added to global_record
        self.assertEqual(len(global_record), 7)
        for t in ["EU490707", "6273289", "6273290", "6273291", "PKU88159.1", "AAA29796.1", "PKU88155.1"]:
            self.assertIn(t, global_record.keys())
        # Test invalid accession number
        with self.assertRaises(urllib.error.HTTPError):
            retrieve("nuccore", "random", "gb")

    def test_preview(self):
        # Test preview of single nucleotide fasta file
        self.assertEqual(len(preview("nuccore", "EU490707", "fasta")), 1)
        for i in preview("nuccore", "EU490707", "fasta")[0].keys():
            self.assertEqual(len(preview("nuccore", "EU490707", "fasta")[0][i].keys()), 5)
        # Test preview of single protein fasta file
        self.assertEqual(len(preview("protein", "PKU88159.1", "fasta")), 1)
        for j in preview("protein", "PKU88159.1", "fasta")[0].keys():
            self.assertEqual(len(preview("protein", "PKU88159.1", "fasta")[0][j].keys()), 5)
        # Test preview of multiple nucleotide genbank files
        self.assertEqual(len(preview("nuccore", "6273289,6273290,6273291", "gb")), 3)
        for k in preview("nuccore", "6273289,6273290,6273291", "gb")[0].keys():
            self.assertEqual(len(preview("nuccore", "6273289,6273290,6273291", "gb")[0][k].keys()), 5)
        # Test preview of multiple protein genprot files
        self.assertEqual(len(preview("protein", "AAA29796.1,PKU88155.1", "gp")), 2)
        for k in preview("protein", "AAA29796.1,PKU88155.1", "gp")[0].keys():
            self.assertEqual(len(preview("protein", "AAA29796.1,PKU88155.1", "gp")[0][k].keys()), 5)
        # Test invalid accession number
        with self.assertRaises(urllib.error.HTTPError):
            preview("nuccore", "random", "gb")


if __name__ == '__main__':
    unittest.main()
