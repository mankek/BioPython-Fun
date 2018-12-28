This project is expanding on the work I did in Dash with Biopython; it aims to apply the similar functionality within an
expanded, more involved application using the Flask framework. This version is still more "proof-of-concept" than anything, and 
I have plans to expand it into the Django framework once I have it reasonably layed out and functional.

Once cloned, navigate into the project directory and run the following command:

	py -3 app.py

the flask application will run on localhost:5000.

Help menu and chart functionality currently unavailable. Available functions:

"Preview" any number of files from the NCBI Nucleotide database using their accession numbers (this doesn't download the files)

Download any number of files from the NCBI Nucleotide database using their accession numbers

Upload a file from any location within the local directory into the application (which just makes a local copy to make it easier 
to work with in future 
functionalities)

All downloaded files can be found in the Files directory within the App directory of the application.

No virtual environment or requirements file yet, so you'll need Flask, Python 3, and Biopython already installed on your 
machine.
