#!/usr/bin/env python

import os
from Bio import SeqIO

def split_fasta(file_name, output_base, output_directory):
    count = 0
    with open(file_name, "rU") as input_handle:
        records = []
        for num, record in enumerate(SeqIO.parse(input_handle, "fasta")):
            records.append(record)
            if num and num % 2000 == 0:
                count += 1
                output_name = "{}/{}_{}.fa".format(output_directory, output_base, count)
                with open(output_name, "w+") as output_handle:
                    SeqIO.write(records, output_handle, "fasta")
                records = []

def main():
    import argparse
    file_name = "x_extracted_allpaths.fa"
    output_base = "x_kian8.4genomen_split"
    output_directory = "/split_fasta"
    split_fasta(file_name, output_base, output_directory)

if __name__ == "__main__":
    main()
