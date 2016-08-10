#!/usr/bin/env python

import os
import subprocess as sp
from Bio import SeqIO

def gather_hits(masked_input_fasta, masked_output_fasta, hits_folder):
    """Gathers hits from all hits files in a directory and uses their ids to \
    collect corresponding fastas from a reference fasta.  Merges non-hit \
    sequences into a new fasta file.

    Args:
        masked_input_fasta (str): A fasta to collect hit fastas from.
        masked_output_fasta (str): A fasta made of fasta hits \
        from the masked_input_fasta.
        hits_folder (str): A folder of hits files.

    Returns:
        None

    Examples:
        gather_hits(
            "/path/to/masked_fasta.fa",
            "/path/to/newly_made/x_rm_masked.fa",
            "/path/to/hits_output_directory"
        )
    """

    records = []
    count = 0
    hits_files = ["{}/{}".format(hits_folder, i) \
                  for i in os.listdir(hits_folder)]
    hits_set = set()
    for hits_file in hits_files:
        with open(hits_file) as input_handle:
            for line in input_handle:
                split_line = line.split(",")
                scaffold_name = split_line[0]
                aln_length = split_line[3]
                hits_set.add(scaffold_name)

    with open(masked_input_fasta, "rU") as input_handle:
        for num, record in enumerate(SeqIO.parse(input_handle, "fasta")):
            if record.id not in hits_set:
                records.append(record)

    with open(masked_output_fasta, "w+") as output_handle:
        SeqIO.write(records, output_handle, "fasta")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Gathers hits from blast.')
    parser.add_argument(
        '-masked_input_fasta',
        type=str,
        required=True,
        help='A fasta to collect hit fastas from.'
    )
    parser.add_argument(
        '-masked_output_fasta',
        type=str,
        required=True,
        help='A fasta made of fasta hits from the masked_input_fasta.'
    )
    parser.add_argument(
        '-hits_folder',
        type=str,
        required=True,
        help='A folder of hits files.'
    )
    args = parser.parse_args()

    gather_hits(
        args.masked_input_fasta,
        args.masked_output_fasta,
        args.hits_folder
    )

if __name__ == "__main__":
    main()
