#!/usr/bin/env python
import argparse
import extract_autosome as ea
from os.path import basename

def main():
    """Runs through masked and unmasked genomic fastas searching for sequence
    hits, gathers hits. Outputs masked and unmasked genomic fastas corresponding
    to contig hits.

    Shell Args:
        masked_genomic_fasta (str): Output fasta from gather_hits.
        unmasked_genomic_fasta (str): Orignal fasta from genomic assembly.
        split_output_base_name (str): Unmasked fasta file to be output.
        split_output_directory (str): Directory to output split fastas.
        db_names (list): Path or paths to blast databases to be run in order.
        hits_directory (str): Directory to store hits.
        masked_output_fasta (str): Basename of masked output fasta.
        unmasked_output_fasta (str): Full path for unmasked output fasta
        cores (int): Number of cores on which to run.
    Returns:
        None

    Usage: extract_autosome.py [-h] -masked_genomic_fasta MASKED_GENOMIC_FASTA
                           -unmasked_genomic_fasta UNMASKED_GENOMIC_FASTA
                           -split_fa_base_name SPLIT_FA_BASE_NAME
                           -split_output_directory SPLIT_OUTPUT_DIRECTORY
                           -db_names DB_NAMES [DB_NAMES ...] -hits_directory
                           HITS_DIRECTORY -masked_output_fasta
                           MASKED_OUTPUT_FASTA -unmasked_output_fasta
                           UNMASKED_OUTPUT_FASTA -cores CORES
    """
    parser = argparse.ArgumentParser(
        description='Runs an autosome extraction pipeline.'
    )
    parser.add_argument(
        '-masked_genomic_fasta',
        type=str,
        required=True,
        help='Masked input fasta to be filtered.'
    )
    parser.add_argument(
        '-unmasked_genomic_fasta',
        type=str,
        required=True,
        help='Unmasked input fasta to be filtered.'
    )
    parser.add_argument(
        '-split_fa_base_name',
        type=str,
        required=True,
        help='Base name for split fasta output.'
    )
    parser.add_argument(
        '-split_output_directory',
        type=str,
        required=True,
        help='Directory to output split fastas.'
    )
    parser.add_argument(
        '-db_names',
        nargs="+",
        required=True,
        help='Path or multiple paths to blast databases to be run in order.'
    )
    parser.add_argument(
        '-hits_directory',
        type=str,
        required=True,
        help='Directory to store hits.'
    )
    parser.add_argument(
        '-masked_output_fasta',
        type=str,
        required=True,
        help='Basename of masked output fasta.'
    )
    parser.add_argument(
        '-unmasked_output_fasta',
        type=str,
        required=True,
        help='Full path for unmasked output fasta'
    )
    parser.add_argument(
        '-cores',
        type=int,
        required=True,
        help='Number of cores on which to run.'
    )

    args = parser.parse_args()

    for database in args.db_names:
        db_base_name = basename(db_name)
        args.masked_output_fasta = "{}_{}".format(db_base_name,
                                             args.masked_output_fasta)
        ea.extract_autosome(
            args.masked_genomic_fasta,
            args.split_fa_base_name,
            args.split_output_directory,
            args.db_name,
            args.hits_directory,
            args.masked_output_fasta,
            cores=args.cores
        )
        args.masked_input_fasta = args.masked_output_fasta

    ea.unmask_autosome(
        args.masked_output_fasta,
        args.unmasked_genomic_fasta,
        args.unmasked_output_fasta
    )

if __name__ == "__main__":
    main()
