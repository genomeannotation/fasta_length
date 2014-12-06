#!/usr/bin/env python
import sys
import numpy as np
from src.fasta_reader import read_fasta

def print_histogram(lengths, bin_size):
    histogram = {}
    max_length = max(lengths)
    bins = []
    i = 0
    while i*bin_size < max_length + bin_size:
        bins.append(i*bin_size)
        i += 1
    histo = np.histogram(lengths, bins)
    print(histo[0])

    #for length in lengths:
        #if length in histogram:
            #histogram[length] += 1
        #else:
            #histogram[length] = 1
    return histogram

def histogram(bin_size, lengths_dict):
    counts_dict = {}
    # get max of all lengths lists
    # make list of bins based on max length and bin size
    # for test will be [0, 100, 200]
    # for each taxa in the dictionary ...
    #   np.hist(lengths, bins) where lengths is lengths_dict[taxa]
    #   first result is counts
    #   update counts dict with list of counts
    
    # to access a list of dictionary keys: dict.keys() ["taxa1", "taxa2"]
    # to access a list of dictionary values: dict.values() [[150], [50, ...
    # to iterate over keys and values, you can do
    #    for k, v in dict.items():
    #      print(k)
    #      print(v + "\n")
    #    (now add "\n")

    # taxa = dict.keys()
    # header = "\t".join(taxa)
    # header += "\n"

    return "here you go"

def run_test():
    test_dict = {"taxon1": [150], "taxon2": [50, 105, 110, 115, 250, 251]}
    bin_size = 100
    expected = "bins\ttaxon1\ttaxon2\n"
    expected += "0\t0\t1\n"
    expected += "100\t1\t3\n"
    expected += "200\t0\t2\n"
    actual = histogram(bin_size, test_dict)
    print(expected)
    print(actual)
    print("")
    if expected != actual:
        print("fail")

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "test":
            run_test()
            sys.exit()
        else:
            sys.stderr.write("Usage: fasta_length.py <bin_size> <fasta1> <fasta2> <fasta3> ...\n")
            sys.exit()

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: fasta_length.py <bin_size> <fasta1> <fasta2> <fasta3> ...\n")
        sys.exit()
        
    bin_size = int(sys.argv[1])
    
    #Create dictionary
    All_taxa_read_lengths = {}
    max_length = 0
    
    for arg in sys.argv[2:]:
        #Take name of argument (all words before .fa or .fasta) and turn that into a variable
        taxa = arg.strip().split(".")[0]
        #Create list for read lengths associated with taxa
        taxa_read_length_list = []
        with open(arg, "r") as fasta:
            seqs = read_fasta(fasta)
            for seq in seqs:
                read_length = len(seq.bases)
                taxa_read_length_list.append(read_length)
                taxa_read_length_list.sort()
                if taxa in All_taxa_read_lengths:
                    pass
                else:
                    All_taxa_read_lengths[taxa] = taxa_read_length_list
                this_max = max(taxa_read_length_list)
                if this_max > max_length:
                    max_length = this_max
    print("max length is " + str(max_length))
    #Add key and list to dictionary
    #print (All_taxa_read_lengths)
    print_histogram(taxa_read_length_list, bin_size)

##################################3

if __name__ == "__main__":
    main()

#Make and plot histogram with plt.hist()
#plst.hist(All_taxa_read_lengths, bins=bin_size)
