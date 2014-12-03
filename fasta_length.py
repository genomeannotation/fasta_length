#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
from src.fasta_reader import read_fasta

def main():
    if len(sys.argv) == 1:
        print("Usage: fasta_length.py <bin_size> <fasta1> <fasta2> <fasta3> ...")
        
    for arg in sys.argv[1]:
        bin_size = sys.argv[1]
        
    for arg in sys.argv[2:]:
        with open(arg, 'r') as fasta:
            seqs = read_fasta(fasta)
            for seq in seqs:
                pass

##################################3

if __name__ == "__main__":
    main()
    
#Create list that holds values to be binned with plt.hist()
Read_length_list = []

#Add reads to list
Read_length_list.append(Read_lengths)

#Make and plot histogram with plt.hist()
plst.hist(Read_length_list, bins=bin_size)
