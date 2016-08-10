#!/usr/bin/env python
from extract_unmapped import unmask_autosome
from gather_hits import gather_hits
from run_blast import run_blast
from split_fasta import split_fasta

def extract_autosome(masked_query_fasta, output_name_base,
                     split_output_directory, db_name, hits_directory,
                     masked_output_fasta):
    """Runs fasta splittings, blast, and hits gathering functions to produce \
    a masked output fasta based on blast results against the specified blast \
    database

    Args:
        masked_query_fasta (str):
        output_base_name (str):
        split_output_directory (str):
        db_name (str):
        hits_directory (str):
        masked_output_fasta (str):

    Returns:
        None

    Examples:
        extract_autosome(
            "/path/to/masked/fasta",
            "kian8.4_fasta_splits",
            "/path/to/split_output_directory",
            "xchr",
            "/path/to/hits_output_directory",
            "/where/to/output/masked_output.fasta"
        )
    """
    split_fasta(masked_query_fasta, output_name_base, split_output_directory)
    run_blast(split_output_directory, db_name, hits_directory, cores=1)
    gather_hits(masked_query_fasta, masked_output_fasta, hits_directory)
