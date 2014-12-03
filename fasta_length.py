#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
from src.fasta_reader import read_fasta

def main():
    if len(sys.argv) < 2:
        print("Usage: fasta_length.py <bin_size> <fasta1> <fasta2> <fasta3> ...")
        
    bin_size = int.(sys.argv[1])
    
    #Create dictionary
    All_taxa_read_lengths = {}
    
    for arg in sys.argv[2:]:
        Read_length_list = []
        with open(arg, 'r') as fasta:
            seqs = read_fasta(fasta)
            for seq in seqs:
                Read_length = len(seq.bases)
                Read_length_list.append(Read_length)

##################################3

if __name__ == "__main__":
    main()

#Make and plot histogram with plt.hist()
plst.hist(Read_length_list, bins=bin_size)
