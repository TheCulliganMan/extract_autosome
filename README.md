# Extract Autosome
##What it does:
Extract autosome uses biopython and blast to extract sequence matches from large
fasta files.  Repeat masking is recommended before running this pipeline.
##How it works:
  1. Split large fasta files into smaller pieces.  
  2. Run search pieces for a fasta sequence using blast.
  3. Collect blast hits from each blast run.
  4. Create new fasta files using the contig id's from non-hit contigs.
