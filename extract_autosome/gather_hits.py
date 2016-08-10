#!/usr/bin/env python

import os
import subprocess as sp
from Bio import SeqIO

def gather_hits(unmasked_fasta, output_fasta, hits_folder):
    records = []
    count = 0
    hits_files = ["{}/{}".format(hits_folder, i) for i in os.listdir(hits_folder)]
    hits_set = set()
    for hits_file in hits_files:
        with open(hits_file) as input_handle:
            for line in input_handle:
                split_line = line.split(",")
                scaffold_name = split_line[0]
                aln_length = split_line[3]
                hits_set.add(scaffold_name)

    with open(unmasked_fasta, "rU") as input_handle:
        for num, record in enumerate(SeqIO.parse(input_handle, "fasta")):
            if record.id not in hits_set:
                records.append(record)

    with open(output_fasta, "w+") as output_handle:
        SeqIO.write(records, output_handle, "fasta")

def main():
    import argparse
    unmasked_fasta = "x_extracted_allpaths.fa"
    output_fasta = "y_x_extracted_allpaths.fa"
    hits_folder = "hits"
    gather_hits(unmasked_fasta, output_fasta, hits_folder)


if __name__ == "__main__":
    main()
