#!/usr/bin/env python
import sys
import numpy as np
from src.fasta_reader import read_fasta

def counts_histogram(bin_size, lengths_dict):
    counts_dict = {}
    proportions_dict = {}
    # get max of all lengths lists
    all_v = []
    for keys, values in lengths_dict.items():
        for value in values:
            all_v.append(value)
    max_length = max(all_v)
    # make list of bins based on max length and bin size
    # for test will be [0, 100, 200]
    bins = []
    i = 0
    while i*bin_size < max_length + bin_size:
       bins.append(i*bin_size)
       i += 1
    for keys, values in lengths_dict.items():
        for value in values:
            counts = np.histogram(values, bins)
            counts_sum = sum(counts[0])
            counts_dict[keys] = counts[0].tolist()
            proportions_dict[keys] = ((counts[0]/counts_sum)*100).tolist()

    # print(counts_dict)
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

    # for k, v in lengths_dict.items():
    #    counts = np.histogram(v, bins) 

    keys = list(counts_dict.keys())
    values = list(counts_dict.values())
    keys.insert(0, "Bins")
    values.insert(0, bins)
    counts_output = '\t'.join(keys)
    counts_output += '\n'
    counts_output += '\n'.join(['\t'.join([str(i) for i in cols]) for cols in zip(*values)])
    proportions = list(proportions_dict.values())
    proportions.insert(0, bins)
    proportions_output = '\t'.join(keys)
    proportions_output += '\n'
    proportions_output += '\n'.join(['\t'.join([str(i) for i in cols]) for cols in zip(*proportions)])
    return (counts_output, proportions_output)

def run_test():
    test_dict = {"taxon1": [150], "taxon2": [50, 105, 110, 115, 250, 251]}
    bin_size = 100
    expected = "bins\ttaxon1\ttaxon2\n"
    expected += "0\t0\t16.6\n"
    expected += "100\t100\t50\n"
    expected += "200\t0\t33.3\n"
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
            sys.stderr.write("Usage: fasta_length.py <output_name> <bin_size> <fasta1> <fasta2> <fasta3> ...\n")
            sys.exit()

    if len(sys.argv) < 4:
        sys.stderr.write("Usage: fasta_length.py <output_name> <bin_size> <fasta1> <fasta2> <fasta3> ...\n")
        sys.exit()
        
    prefix = sys.argv[1]

    bin_size = int(sys.argv[2])

    #Create dictionary
    All_taxa_read_lengths = {}
    max_length = 0
    
    for arg in sys.argv[3:]:
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
    # Add key and list to dictionary
    counts_out = prefix + "_length_counts.txt"
    
    counts_output, proportions_output = counts_histogram(bin_size, All_taxa_read_lengths) 
    with open(counts_out, "w") as first:
        first.write(str(counts_output))

    proportions_out = prefix + "_length_proportions.txt"

    with open(proportions_out, "w") as second:
        second.write(str(proportions_output))

###################################

if __name__ == "__main__":
    main()
