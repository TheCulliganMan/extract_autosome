# Extract Autosome
##What it does:
Extract autosome uses biopython and blast to extract sequence matches from large
fasta files.  Repeat masking is recommended before running this pipeline.
##How it works:
  1. Split large fasta files into smaller pieces.  
  2. Run search pieces for a fasta sequence using blast.
  3. Collect blast hits from each blast run.
  4. Create new fasta files using the contig id's from non-hit contigs.
##Usage:
  1. Install ncbi-blast+, RepeatMasker, and biopython.
  2. Download a reference fasta that you would like to remove from your
  sequence. We used the [Human X Chromosome](ftp://ftp.ncbi.nlm.nih.gov/genomes//H_sapiens/CHR_X/hs_alt_CHM1_1.1_chrX.fa.gz):

  ftp://ftp.ncbi.nlm.nih.gov/genomes//H_sapiens/CHR_X/hs_alt_CHM1_1.1_chrX.fa.gz

  3. Make a blast database for your reference sequence.

  ```bash
  gunzip hs_alt_CHM1_1.1_chrX.fa.gz;
  makeblastdb -in hs_alt_CHM1_1.1_chrX.fa.gz -dbtype nucl;
  ```

  4. In Python, run the extract autosome commands on your genomic sequence
  and the blast db.
  ```python
  import extract_autosome

  extract_autosome.extract_autosome(
    "../blast_x_vs_mick/final.contigs.fasta.masked",
    "mick_output_test_split",
    "fasta_splits",
    "../blast_x_vs_mick/hs_alt_CHM1_1.1_chrX",
    "hits",
    "x_removed.final.contigs.masked.fasta",
    cores=32
  )

  extract_autosome.unmask_autosome(
    "x_removed.final.contigs.masked.fasta",
    "../blast_x_vs_mick/final.contigs.fasta",
    "x.removed.final.contigs.fasta"
  )
  ```
The command above will remove hs_alt_CHM1_1.1_chrX.fa sequence matches from the
final.contigs.fasta file and output to x.removed.final.contigs.fasta.

## Comand Line
There are also the option to run extractions from the command prompt. The
arguments are listed below.

```bash
python extract_autosome.py [-h] -masked_genomic_fasta MASKED_GENOMIC_FASTA
                           -unmasked_genomic_fasta UNMASKED_GENOMIC_FASTA
                           -split_fa_base_name SPLIT_FA_BASE_NAME
                           -split_output_directory SPLIT_OUTPUT_DIRECTORY
                           -db_names DB_NAMES [DB_NAMES ...] -hits_directory
                           HITS_DIRECTORY -masked_output_fasta
                           MASKED_OUTPUT_FASTA -unmasked_output_fasta
                           UNMASKED_OUTPUT_FASTA -cores CORES
 Arguments:
   -h, --help            show this help message and exit
   -masked_genomic_fasta MASKED_GENOMIC_FASTA
                         Masked input fasta to be filtered.
   -unmasked_genomic_fasta UNMASKED_GENOMIC_FASTA
                         Unmasked input fasta to be filtered.
   -split_fa_base_name SPLIT_FA_BASE_NAME
                         Base name for split fasta output.
   -split_output_directory SPLIT_OUTPUT_DIRECTORY
                         Directory to output split fastas.
   -db_names DB_NAMES [DB_NAMES ...]
                         Path or multiple paths to blast databases to be run in
                         order.
   -hits_directory HITS_DIRECTORY
                         Directory to store hits.
   -masked_output_fasta MASKED_OUTPUT_FASTA
                         Basename of masked output fasta.
   -unmasked_output_fasta UNMASKED_OUTPUT_FASTA
                         Full path for unmasked output fasta
   -cores CORES          Number of cores on which to run.
```
