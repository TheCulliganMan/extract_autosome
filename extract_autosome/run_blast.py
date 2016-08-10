#!/usr/bin/env python

from multiprocessing import Pool
import os
import subprocess as sp

def run_blast(blast_folder, db_name, hits_directory, cores=1):
    blast_fastas = [("{}/{}".format(blast_folder, i), i) \
                    for i in os.listdir(blast_folder)]

    blast_commands = []

    for fasta, name in blast_fastas:
        output_name = "{}/{}_{}.hits".format(hits_directory, name, db_name)
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

    parser.add_argument('-blast_folder', type=str, required=True)
    parser.add_argument('-db_name', type=str, required=True)
    parser.add_argument('-hits_directory', type=str, required=True)
    parser.add_argument('-cores', type=int, default=1)
    args = parser.parse_args()

    run_blast(
        args.blast_folder,
        args.db_name,
        args.hits_directory,
        cores=args.cores
    )

if __name__ == '__main__':
    main()
