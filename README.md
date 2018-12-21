Scripts and files for and relating to a Dash application for graphing information in a FASTA file.

Requirements:
Biopython
Plotly
Dash

Running the application
 after cloning, navigate into the directory and run the following command:

    py -3 app.py

The application will run on localhost:8050

Features:

The application allows you to upload a local (inside the application directory) FASTA file and choose from two different graphical analyses.

Skew graph

This scatter graph shows the skew of G and C nucleotides in the sequence; positive growth indicates increasing amounts of G
and negative growth indicates increasing amounts of C.

Nucleotide Composition Graph

This graph counts the amount of each nucleotide in the sequence and displays the amounts as a bar graph.