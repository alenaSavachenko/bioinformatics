# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:27:14 2024

@author: Mijn-PC
"""

E_VALUE_THRESH = 1e-0
for record in NCBIXML.parse(open("results2.xml")): 
     if record.alignments: 
        print("\n") 
        print("query: %s" % record.query[:100]) 
        for align in record.alignments: 
           for hsp in align.hsps: 
              if hsp.expect < E_VALUE_THRESH: 
                 print("match: %s " % align.title[:100])
                 with open('blast_results2.txt', 'a') as file:
                     file.write('\n'+ "query: %s" % record.query[:100] +"\n"+ "match: %s " % align.title[:100] )
                     file.close()