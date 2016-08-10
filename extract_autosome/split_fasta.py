#!/usr/bin/env python

import os
from Bio import SeqIO

def split_fasta(masked_input_fasta, output_base_name, fasta_output_directory):
    count = 0
    with open(masked_input_fasta, "rU") as input_handle:
        records = []
        for num, record in enumerate(SeqIO.parse(input_handle, "fasta")):
            records.append(record)
            if num and num % 2000 == 0:
                count += 1
                output_name = "{}/{}_{}.fa".format(fasta_output_directory,
                                                   output_base_name, count)
                with open(output_name, "w+") as output_handle:
                    SeqIO.write(records, output_handle, "fasta")
                records = []

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Splits a fasta sequence into 2000 contig chunks'
    )
    parser.add_argument('-masked_input_fasta', type=str, required=True)
    parser.add_argument('-output_base_name', type=str, required=True)
    parser.add_argument('-fasta_output_directory', type=str, required=True)
    parser.parse_args()

    split_fasta(
        args.masked_input_fasta,
        args.output_base_name,
        args.fasta_output_directory
    )

if __name__ == "__main__":
    main()
