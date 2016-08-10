#!/usr/bin/env python

from multiprocessing import Pool
import os
import subprocess as sp

def run_blast(blast_folder, db_name, hits_directory, cores=1):
    blast_fastas = [("{}/{}".format(blast_folder, i), i) for i in os.listdir(blast_folder)]

    blast_commands = []

    for fasta, name in blast_fastas:
        output_name = "{}/{}_{}.hits".format(hits_directory, name, db_name)
        blast_command = ["blastn", "-db", db_name, "-query", fasta, "-out", output_name, "-outfmt", "10", '-evalue', "5"]
        blast_commands.append(blast_command)

    pool = Pool(cores)
    pool.map(sp.call, blast_commands)
    pool.close()
    pool.join()

def main():
    import argparse
    blast_folder = "split_genome"
    db_name = "x"
    hits_directoy = "hits"
    cores = 31
    run_blast(blast_folder, db_name, hits_directoy, cores=cores)

if __name__ == '__main__':
    main()
