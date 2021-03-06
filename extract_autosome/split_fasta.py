#!/usr/bin/env python

import os
import shutil
from Bio import SeqIO

def split_fasta(masked_input_fasta, output_base_name,
                fasta_output_directory, overwrite=True):
    """Takes in a fasta and splits it every 2000 records.

    Args:
        masked_input_fasta (str): Masked genomic sequence (fasta).
        output_base_name (str): Split fastas will be renamed to this base.
        fasta_output_directory (str): Directory to output split fastas.
        overwrite (bool): Overwrite directories (default True)

    Returns:
        None

    Examples:
        split_fasta(
            "/path/to/masked_input_fasta.fa",
            "kian_8.4_split_2000",
            "/output/path/split_fasta_out"
        )
    """
    count = 0
    if overwrite:
        if os.path.isdir(fasta_output_directory):
            shutil.rmtree(fasta_output_directory)
    else:
        assert os.path.isdir(fasta_output_directory), \
            "You cannot overwrite {} file.".format(fasta_output_directory)
    os.makedirs(fasta_output_directory)

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
    parser.add_argument(
        '-masked_input_fasta',
        type=str,
        required=True,
        help="Masked genomic sequence (fasta)"
    )
    parser.add_argument(
        '-output_base_name',
        type=str,
        required=True,
        help="Split fastas will be renamed to this base."
    )
    parser.add_argument(
        '-fasta_output_directory',
        type=str,
        required=True,
        help="Directory to output split fastas."
    )
    parser.add_argument(
        '-overwrite',
        type=bool,
        default=True,
        help='Overwrite directories (default True).'
    )

    args = parser.parse_args()

    split_fasta(
        args.masked_input_fasta,
        args.output_base_name,
        args.fasta_output_directory,
        overwrite=args.overwrite
    )

if __name__ == "__main__":
    main()
