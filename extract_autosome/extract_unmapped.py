#!/usr/bin/env python
from __future__ import print_function
import os
import subprocess as sp
from Bio import SeqIO

def extract_unmapped(masked_file, unmasked_file, output_name)
    record_set = set()
    all_count = 0
    with open(masked_file, "rU") as input_handle:
        records = []
        for record in SeqIO.parse(input_handle, "fasta"):
            record_set.add(record.id)

    print (len(record_set), "Contigs in X-Y Selection.")

    with open(unmasked_file, "rU") as input_handle:
        with open(output_name, "w+") as output_handle:
            for record in SeqIO.parse(input_handle, "fasta"):
                all_count += 1
                if record.id in record_set:
                    SeqIO.write(record, output_handle, "fasta")

    print (all_count, "Contigs Total.")

def main():
    import argparse
    masked_file = "y_x_extracted_allpaths.fa"
    unmasked_file = "final.contigs.fasta"
    output_name = "y_x_extracted.final.contigs.fasta"

if __name__ == "__main__":
    main()
