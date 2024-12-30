

# create soft link

ln -s genemark.f.good.gtf  bonafide.gtf


# compute flanking regions

computeFlankingRegion.pl bonafide.gtf


# this wil produce output:

# Total length gene length (including introns): 1780572. Number of genes: 1975. Average Length: 901.555443037975
# The flanking_DNA value is: 450 (the Minimum of 10 000 and 450)
# next step is to get bonafide.gb trainingset

gff2gbSmallDNA.pl bonafide.gtf genome.fa 450 tmp.gb
filterGenesIn_mRNAname.pl bonafide.gtf tmp.gb > bonafide.gb

# bonafide.gb is now in the map processing