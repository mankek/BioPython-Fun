#!/usr/bin/python
import unittest
from App.methods import get_db, guess_database
import os


class TestDataProcess(unittest.TestCase):

    def setUp(self):
        # Make a file with an appropriate extension, but no content
        with open(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files\Empty_file.gb", 'w') as empty_file:
            empty_file.write("\n")
        empty_file.close()

        # Make a file with an inappropriate extension
        with open(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files\Wrong_file.txt", 'w') as wrong_file:
            wrong_file.write("\n")
        wrong_file.close()

    def test_database_names(self):
        # Test that the displayed database options pass
        self.assertEqual(get_db("nuccore"), "Nucleotide")
        self.assertEqual(get_db("protein"), "Protein")
        self.assertEqual(get_db("NA"), "Not Available")
        # Test that an unavailable database option raises an error
        with self.assertRaises(KeyError):
            get_db("Random")

    def test_database_guess(self):
        # Test that each file yields the correct database
        for i, k in zip(["6273289.gb", "AAA29796.1.gp", "EU490707.fasta", "PKU88159.1.fasta"],
                        ["nuccore", "protein", "nuccore", "protein"]):
            file_in = os.path.join(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files", i)
            self.assertEqual(guess_database(file_in), k)
        # Test that the incorrect files raise exceptions
        self.assertEqual(guess_database(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files\Empty_file.gb"), None)
        with self.assertRaises(ValueError):
            guess_database(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files\Wrong_file.txt")

    def tearDown(self):
        # Remove all files so that all tests can be run again
        os.remove(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files\Empty_file.gb")
        os.remove(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files\Wrong_file.txt")
        for _,_, s in os.walk(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files"):
            if s:
                for t in s:
                    os.remove(os.path.join(r"C:\Users\krmanke\PycharmProjects\FASTA_analysis\App\Files", t))


if __name__ == '__main__':
    unittest.main()
