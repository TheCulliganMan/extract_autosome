#!/usr/bin/env python
from __future__ import print_function
import os
import subprocess as sp
from Bio import SeqIO

def unmask_autosome(masked_output_fasta, unmasked_query_fasta,
                    unmasked_output_fasta):
    record_set = set()
    all_count = 0
    with open(masked_output_fasta, "rU") as input_handle:
        records = []
        for record in SeqIO.parse(input_handle, "fasta"):
            record_set.add(record.id)

    print (len(record_set), "Contigs in X-Y Selection.")

    with open(unmasked_query_fasta, "rU") as input_handle:
        with open(unmasked_output_fasta, "w+") as output_handle:
            for record in SeqIO.parse(input_handle, "fasta"):
                all_count += 1
                if record.id in record_set:
                    SeqIO.write(record, output_handle, "fasta")

    print (all_count, "Contigs Total.")

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Takes an unmasked fasta and a masked fasta selection and \
        builds an unmasked fasta selection.'
    )
    parser.add_argument('-masked_output_fasta', type=str, required=True)
    parser.add_argument('-unmasked_query_fasta', type=str, required=True)
    parser.add_argument('-unmasked_output_fasta', type=str, required=True)
    parser.parse_args()

    unmask_autosome(
        args.masked_output_fasta,
        args.unmasked_query_fasta,
        args.unmasked_output_fasta
    )

if __name__ == "__main__":
    main()
