#!/usr/bin/env python
import sys
from src.fasta_reader import read_fasta

def main():
    if len(sys.argv) == 1:
        print("Usage: fasta_length.py <fasta1> <fasta2> <fasta3> ...")

    for arg in sys.argv[1:]:
        with open(arg, 'r') as fasta:
            seqs = read_fasta(fasta)
            for seq in seqs:
                pass

##################################3

if __name__ == "__main__":
    main()
