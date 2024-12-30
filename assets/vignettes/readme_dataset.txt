 Dataset includes 5 csv files (media 1-5), contains RNA sequencing data generated for MCF7 cells.  
 Author : Ying Chen
 date: this version posted April 22, 2021
 source: https://www.biorxiv.org/content/10.1101/2021.04.21.440736v1
 
 Dataset contains list of  variables:


Media1

NanoporeSamples
Sample (string)
Sequencing platform (string)
Sequencing flowcell (string)
Barcoding kit(string)
Sequencing kit(string)
Sequencing protocol(string)
Cell growth(string)
RNA extraction(string)
Cell line(string)
PolyA selection(string)
Spike in concentration (procent)
Extra notes(string)

ShortReadSamples
Sample
Cell line
Library preparation
Sequencing protocol
Spike in concentration


Media2

ensembl_gene_id (string)
hgnc_symbol(string)
gene_biotype (string)
description (string)
chromosome_name (int)
start_position (int)
end_position (int)
strand (int)
meanCount.cdna (double)
meanCount.dcdna (double)
meanCount.drna (double)
setBiasCandidates (boolean) 
meanCoverage.cdna(double))
meanCoverage.dcdna (double))
meanCoverage.drna (double))
z_score.cdna.dcdna (double))
adjPval.cdna.dcdna (double)
z_score.cdna.drna(double)
adjPval.cdna.drna (double)
z_score.dcdna.drna (double)
adjPval.dcdna.drna(double)
significant_comparison (string)


Media3

gene_name (string)
strand (+/-)
cellLine (string)
txMajor (string)
txMinor (string)
altFirstExon (boolean)
altLastExon (boolena)
intronRetention (boolean)
exonSkipping (boolean)
altSplicing5Prime (boolean)
altSplicing3Prime (boolean)
txMajorFullLengthSupport (int)
txMinorFullLengthSupport (int)
txMajorFullLengthAveEstimates(boolean)
txMinorFullLengthAveEstimates(boolean)
geneAverageEstimates(boolean)


Media4

gene_name (string)
tx_name (tring)
chrom_name (int)
strand (+/-)
start (int)
end( int)
transcript_type (string)
repeat_content (double)
A549Expression (double)
Hct116Expression (double)
HepG2Expression (double)
K562Expression (double)
MCF7Expression (double)

Media5

fusion_gene (string)
cellLine (string)
3PrimeGene_allCount (double)
5PrimeGene_allCount (double)
fusionGene_allCount (double)
3PrimeGene_flCount (double)
5PrimeGene_flCount (double)
fusionGene_flCount (double)
log2Reads (double)
Breakpoints (int)
Illumina (boolean)
Mitelman (boolean)
Validated (boolean)
BreakpointClass (double)

