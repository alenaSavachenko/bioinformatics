

# the genemark has produced file gtf, containing lines whith start and end coordinate of genes:
# OX457036.1 Lumbricus terrestris genome assembly, chromosome: 1	GeneMark.hmm3	gene	127481	128128	.	+	.	gene_id "8_g"; transcript_id "8_t";



# this script  filterGenemark.pl  in the latest distribution gives an error, you have to replace it from the script form other distribution 
#  the working scrpt filterGenemark.pl is in map scrpts. 



perl filterGenemark.pl --genemark genemark.gtf  --introns introns.gff

# this produces this output

#Average gene length: 5146
#Average number of introns: 3.26484477042098
#Good gene rate: 0.198432633376871
#Number of genes: 9972
#Number of complete genes: 9953
#Number of good genes: 1975
#Number of one-exon-genes: 1982
#Number of bad genes: 7997
#Good intron rate: 0
#One exon gene rate (of good genes): 1.00354430379747

# genemark.f.good.gtf is now in the map data_processing

# we have 1975 good genes to build a training set 