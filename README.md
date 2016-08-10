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
  sequence. We used the [Human X Chromosome](ftp://ftp.ncbi.nlm.nih.gov/genomes//H_sapiens/CHR_X/hs_alt_CHM1_1.1_chrX.fa.gz)
  3. Make a blast database for your reference sequence.

  ```bash
  makeblastdb -in hs_alt_CHM1_1.1_chrX.fa.gz -dbtype nucl
  ```
  
  4. Run the extract autosome commands on your genomic sequence and the blast db.
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
The command above will remove x.fa sequence matches from the
final.contigs.fasta file and output to x.removed.final.contigs.fasta
