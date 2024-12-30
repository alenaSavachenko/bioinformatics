# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:26:14 2024

@author: Mijn-PC
"""

import os
cwd = os.getcwd()
print(cwd)

import sys
from Bio.Blast import NCBIXML
#Usage, opens an outfile and then parses any number of .xml files into that outfile, printing all hits
#parse_blastn.py outfile.txt anynumberofinfiles.xml

# file for sorted : "sorted_by_coordinates.fraction2.txt

OUT = open("sorted_by_coordinates.fraction3.txt", 'w')
OUT.write("Query Name\tQuery Length\tAlignment ID NCBI\teValue\n")

#result21-30.xml

# result.nands xml:  blast.results.fraction2.xml


result_handle = open("blast.results.fraction3.xml")
blast_records = NCBIXML.parse(result_handle)
for rec in blast_records:
        for alignment in rec.alignments:
            for hsp in alignment.hsps:
                fields = [rec.query_id, rec.query[:100], str(rec.query_length), alignment.hit_id,
                           alignment.accession, str(hsp.expect)]
                OUT.write("\t".join(fields) + "\n")
OUT.close() 
print('Done')  


