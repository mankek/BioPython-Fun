#!/usr/bin/python
import unittest
from App.methods import global_record, upload, get_files
import os


class TestFileOps(unittest.TestCase):

    def setUp(self):
        # Make a file with an inappropriate extension
        with open(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "App", "Files", "Wrong_file.txt"), 'w') as wrong_file:
            wrong_file.write("\n")
        wrong_file.close()

        # Make a file with an inappropriate extension in the App directory
        with open(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "App", "Wrong_file2.txt"), 'w') as wrong_file2:
            wrong_file2.write("\n")
        wrong_file2.close()

        # Move two files from Files to App directory
        dir_name = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "App")
        os.rename(os.path.join(dir_name, "Files\\EU490707.fasta"),
                  os.path.join(dir_name, "EU490707.fasta"))
        if not os.path.exists(os.path.join(dir_name, "PKU88159.1.fasta")):
            os.rename(os.path.join(dir_name, "Files\\PKU88159.1.fasta"),
                      os.path.join(dir_name, "PKU88159.1.fasta"))

    def test_get_files(self):
        dir_name = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "App")
        self.assertEqual(get_files(), "done")
        # Test that moved files were removed from global record and wrong_file wasn't added
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
        self.assertEqual(upload(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "App",
                                             "EU490707.fasta"), "nuccore"), "done")
        # Test upload of protein file with unspecified database
        self.assertEqual(upload(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "App",
                                             "PKU88159.1.fasta"), "NA"), "done")
        # Test that upload files exist in correct locations
        self.assertTrue(os.path.exists(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "App",
                                                    "Files", "EU490707.fasta")))
        self.assertTrue(os.path.exists(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "App",
                                                    "Files", "PKU88159.1.fasta")))
        # Test that upload files were added to global record
        self.assertEqual(len(global_record), 7)
        for i in ["EU490707", "PKU88159.1"]:
            self.assertIn(i, global_record.keys())
        # Test that upload called guess_database correctly
        self.assertEqual(global_record["PKU88159.1"]["db"], "Protein")
        # Test that upload of wrong_file2 doesn't crash application
        self.assertEqual(upload(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "App",
                                             "Wrong_file2.txt"), "protein"), "File doesn't have an accepted extension.")
        # Test that upload of wrong_file2 didn't add to global record
        self.assertEqual(len(global_record), 7)
        self.assertNotIn("Wrong_file2", global_record.keys())


if __name__ == '__main__':
    unittest.main()
