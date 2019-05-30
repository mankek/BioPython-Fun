This project is expanding on the work I did in Dash with Biopython; it aims to apply the similar functionality within an
expanded, more involved application using the Flask framework. This version is still more "proof-of-concept" than anything.

Once cloned, navigate into the project directory and run the following command:

	py -3 app.py

the flask application will run on localhost:5000.

Available functions:

"Preview" up to 10 files from the NCBI Nucleotide database using their accession numbers (this doesn't download the files)

Download up to 10 files from the NCBI Nucleotide database using their accession numbers

Upload a file from any location within the local directory into the application (which makes a copy to Files to make it easier
to work with in other functions)

All downloaded and uploaded files can be found in the Files directory within the App directory of the application.

No virtual environment or requirements file yet, so you'll need Flask, Python 3, and Biopython already installed on your 
machine.

A rudimentary test suite that uses unittest to test the functions found in methods.py is also available; Once the application
has all the functions I'm aiming for, I'll begin implementing logic to deal with exception and error cases.

Navigate to within the project directory and run:

    python -m unittest discover
