#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
from src.fasta_reader import read_fasta

def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: fasta_length.py <bin_size> <fasta1> <fasta2> <fasta3> ...")
        sys.exit()
        
    bin_size = int.(sys.argv[1])
    
    #Create dictionary
    All_taxa_read_lengths = {}
    
    for arg in sys.argv[2:]:
        #Take name of argument (all words before .fa or .fasta) and turn that into a variable
        taxa = arg.strip().split(.)[1]
        #Create list for read lengths associated with taxa
        taxa_read_length_list = []
        with open(arg, 'r') as fasta:
            seqs = read_fasta(fasta)
            for seq in seqs:
                read_length = len(seq.bases)
                taxa_read_length_list.append(read_length)
        #Add key and list to dictionary
        All_taxa_read_lengths["taxa"] = taxa_read_length_list

##################################3

if __name__ == "__main__":
    main()

#Make and plot histogram with plt.hist()
plst.hist(All_taxa_read_lengths, bins=bin_size)
