#!/usr/bin/python
import unittest
from App.methods import retrieve, global_record
import os
import urllib.error


class TestFileGet(unittest.TestCase):

    def setUp(self):
        pass

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
            self.assertTrue(os.path.exists(os.path.join(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files", i + "." + h)))
        # Test that retrieved files were added to global_record
        for t in ["EU490707", "6273289", "6273290", "6273291", "PKU88159.1", "AAA29796.1", "PKU88155.1"]:
            self.assertIn(t, global_record.keys())
            self.assertIn(global_record[t], global_record.values())
        # Test invalid accession number
        with self.assertRaises(urllib.error.HTTPError):
            retrieve("nuccore", "random", "gb")


if __name__ == '__main__':
    unittest.main()
