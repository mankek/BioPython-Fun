#!/usr/bin/python
import unittest
from App.methods import global_record, upload, get_files
import os


class TestFileOps(unittest.TestCase):

    def setUp(self):
        # Move two files from Files to App directory
        dir_name = "C:\\Users\\krmanke\\PycharmProjects\\FASTA_analysis\\App"
        os.rename(os.path.join(dir_name, "Files\\EU490707.fasta"),
                  os.path.join(dir_name, "EU490707.fasta"))
        if not os.path.exists(os.path.join(dir_name, "PKU88159.1.fasta")):
            os.rename(os.path.join(dir_name, "Files\\PKU88159.1.fasta"),
                      os.path.join(dir_name, "PKU88159.1.fasta"))

    def test_get_files(self):
        dir_name = "C:\\Users\\krmanke\\PycharmProjects\\FASTA_analysis\\App"
        # Run function
        get_files()
        # Test that moved files were removed from global record
        self.assertEqual(len(global_record), 5)
        self.assertNotIn("EU490707", global_record.keys())
        self.assertNotIn("PKU88159.1", global_record.keys())
        # Move one of the outside files back into Files
        os.rename(os.path.join(dir_name, "EU490707.fasta"),
                  os.path.join(dir_name, "Files\\EU490707.fasta"))
        # Run function
        get_files()
        # Test that moved file was added to global record
        self.assertEqual(len(global_record), 6)
        self.assertTrue("EU490707" in global_record.keys())

    def test_upload(self):
        # Test upload of nucleotide file with specified database
        self.assertEqual(upload(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\EU490707.fasta", "nuccore"), "done")
        # Test upload of protein file with unspecified database
        self.assertEqual(upload(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\PKU88159.1.fasta", "NA"), "done")
        # Test that upload files exist in correct locations
        self.assertTrue(os.path.exists(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files\EU490707.fasta"))
        self.assertTrue(os.path.exists(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files\PKU88159.1.fasta"))
        # Test that upload files were added to global record
        self.assertEqual(len(global_record), 7)
        for i in ["EU490707", "PKU88159.1"]:
            self.assertIn(i, global_record.keys())
        # Test that upload called guess_database correctly
        self.assertEqual(global_record["PKU88159.1"]["db"], "Protein")


if __name__ == '__main__':
    unittest.main()