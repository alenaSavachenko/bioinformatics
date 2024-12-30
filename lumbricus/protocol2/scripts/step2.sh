#  Copy genome fasta and Arthoproda.fa to the input map of ProtHints, run in bash from the input map:

../bin/prothint.py  input/genome.fasta  input/Arthropoda.fa

# this will produces output: seed.proteins.fa,  prothints.gff, prothint_augustus.gff. See map data processing, section ProtHints. Seed file can
# be used with startAlign.pl. the hints file can be used as external hints with Augustus

# StartAlign.pl is a part of braker. Change your conda enviroment, where your braker is installed, run this command:

startAlign.pl --genome=genome.fa --prot=seed_proteins.faa --prg=gth

# this wil produce gth.concat.aln, see  data proccessing.
# activate your enviroment, where your augustus and braker are intsalled

gth2gtf.pl  gth.concat.aln bonafide.gtf

# this wil produce bonafide.gtf file, see map data -processing, part Bonafid

 computeFlankingRegion.pl bonafide.gtf

# This gives the following output:
# Total length gene length (including introns): 5412279. Number of genes: 1090. Average Length: 4965.39357798165
#(py27) alena@alena-ThinkPad-L470-W10DG:~/Downloads/ProtHint-master/align_gth$ computeFlankingRegion.pl bonafide.gtf  
# Total length gene length (including introns): 5412279. Number of genes: 1090. Average Length: 4965.39357798165
# The flanking_DNA value is: 2482 (the Minimum of 10 000 and 2482)

# convert to gb file

gff2gbSmallDNA.pl bonafide.gtf genome.fa  2482 bonafide.gb

# this wil output bonafide.gb. See map data procesing, Bonafid

