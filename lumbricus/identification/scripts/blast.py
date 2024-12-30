# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:48:30 2024

@author: Mijn-PC
"""

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


genomic="genome.fa"

sequence_data = open(genomic).read()
 
sequence_data
 
result_handle = NCBIWWW.qblast("blastn", "nt", sequence_data, hitlist_size=5, alignments=50)

result_handle


# result file name: blast.results.fraction2.xm


with open('reults.xml', 'w') as save_file: 
   blast_results = result_handle.read() 
   save_file.write(blast_results)
   


