

# build index name lumter

bowtie2-build -f  Lumbricus_terrestris-GCA_949752735.1-softmasked.fa  lumter  --large-index 

# this will build index files with prefix lumter
# run tophat, where sample1, sample2  your fastq files

tophat lumter     sample_1.fastq  sample_2.fastq \                           
 --output-dir TopHAT \ 
 
 # it wil produces accepted_hits.bam with  Alignment results, A list of read alignments
 # jucntions.bed, A BED track of junctions reported by TopHat. Each junction consists of two connected BED blocks, where each block is as long as the maximal overhang of any read spanning the junction. The score is the number of alignments spanning the junction.
 #  file jucntions.bed, This file will be used for next steps
 # use bed_to_gff.pl from the GeneMark ET distribution to convert aligment file to hints
 
 
 perl  path_to/GeneMarkES/bed_to_gff.pl \
 --bed  path_to/tophat_out/junctions.bed \
 --gff introns.gff  --label TopHat2
   
   
   
# the output file introns.gff contains strand information that can be used for ET trainging
#the output of junctons.bed
#OX457036.1	202801	204722	JUNC00000008	1	+	202801	204722	255,0,0	2	119,32	0,1889
# the output of introns.gff:
#OX457036.1	TopHat2	intron	253060	254504	12	+	.	.
# the file with introns is used to build a genemark model:

 ../../gmes_petap.pl     --verbose --sequence   genome.fa   --ET  introns.gff
 
 # this command wil produce gmhmm.mod, and genemark.gtf, see data proccessing
 
 