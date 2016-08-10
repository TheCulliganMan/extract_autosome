#!/usr/bin/env python
from extract_unmapped import extract_unmapped
from gather_hits import gather_hits
from run_blast import run_blast
from split_fasta import split_fasta

def extract_autosome(masked_query_fasta, output_name_base,
                     split_output_directory, db_name, hits_directory,
                     masked_output_fasta):
    split_fasta(masked_query_fasta, output_name_base, split_output_directory)
    run_blast(split_output_directory, db_name, hits_directory, cores=1)
    gather_hits(masked_query_fasta, masked_output_fasta, hits_directory)

def unmask_autosome(unmasked_output_fasta, unmasked_query_fasta,
                    unmasked_output_fasta):
    extract_unmapped(masked_output_fasta, unmasked_query_fasta,
                     unmasked_output_fasta)
