#!/usr/bin/env python

from multiprocessing import Pool
import os
import subprocess as sp
from os.path import basename

def run_blast(blast_directory, db_name,
              hits_directory, cores=1, overwrite=True):
    """Runs blast on all fastas in a specified directory against a specified \
    blast database.  Collects results in a 'hits' directory.

    Args:
        blast_directory (str): A directory of fasta file to run blast on.
        db_name (str): The location / name of a blast database.
        hits_directory (str): An output directory to store blast output.
        cores (int): Number of cores to run the program on.

    Returns:
        None

    Examples:
        run_blast(
            "/path/to/fasta_directory",
            "xchr",
            "/path/to/hits_output_directory",
            6
        )
    """
    if overwrite:
        if not os.path.isdir(hits_directory):
            os.removedirs(hits_directory)
        os.makedirs(hits_directory)
    else:
        assert os.path.isdir(hits_directory), \
            "You cannot overwrite {} file.".format(hits_directory)


    blast_fastas = [("{}/{}".format(blast_directory, i), i) \
                    for i in os.listdir(blast_directory)]

    blast_commands = []

    for fasta, name in blast_fastas:
        db_base_name = basename(db_name)
        output_name = "{}/{}_{}.hits".format(hits_directory, name, db_base_name)
        blast_command = ["blastn", "-db", db_name, "-query", fasta, "-out",
                         output_name, "-outfmt", "10", '-evalue', "5"]
        blast_commands.append(blast_command)

    pool = Pool(cores)
    pool.map(sp.call, blast_commands)
    pool.close()
    pool.join()

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Runs Blast on all items in a directory.'
    )

    parser.add_argument(
        '-blast_directory',
        type=str,
        required=True,
        help='A directory of fasta file to run blast on.'
    )
    parser.add_argument(
        '-db_name',
        type=str,
        required=True,
        help='The location / name of a blast database.'
    )
    parser.add_argument(
        '-hits_directory',
        type=str,
        required=True,
        help='An output directory to store blast output.'
    )
    parser.add_argument(
        '-cores',
        type=int,
        default=1,
        help='Number of cores to run the program on.'
    )
    args = parser.parse_args()

    run_blast(
        args.blast_directory,
        args.db_name,
        args.hits_directory,
        cores=args.cores
    )

if __name__ == '__main__':
    main()
