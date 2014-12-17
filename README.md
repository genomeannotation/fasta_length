fasta_length
============

This python script reads fasta files and generates a raw count of transcripts or reads histogram table and a proportion of total transcripts/reads histogram table for every taxa included.  

Requires:  
python3
numpy

Usage is as follows: fasta_lengths.py <output file name> <bin sizes> <fasta 1> <fasta 2> <fasta 3> ...

For maximum readability:  
Change the fasta file names to Genus_species.fasta
Note:  All strings before the first "." in a file MUST be unique.  The headers of the output tables will be populated by the string before the first "." in your file name. 

For example, if your file name is D_melanogaster_unfiltered.fasta, the header for that taxa in the resulting tables will be "D_melanogaster_unfiltered."  If you include two files with the names D_melanogaster.unfiltered.fasta and D_melanogaster.fasta, the name associated with the file will be the same "D_melanogaster" and only the one of them will be included in the table.
