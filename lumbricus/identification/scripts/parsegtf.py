# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:15:41 2024

@author: Mijn-PC
"""

import re
import pandas as pd

gff="gff.gff"
parsed="parsed.gff"
genome="genome.gff"


# remove #, removing leading whitespaces

with open(gff, 'r') as infile, open(parsed, 'w') as outfile:
	temp = infile.read().replace("#", "")    
	outfile.write(temp)
    
with open(parsed, 'r') as file:
    for line in file:        
        newline=line.lstrip()        
        with open ("out", "a") as  outf:
            outf.write(newline)
            outf.close() 
                
    
gene_coords = [] 
coding_seq=[]
  
content = open("out", 'r').read()
pattern_a = r'gene.*\s+(OX457036.*AUGUSTUS\sgene.*g\d+)'
matches_a = re.findall(pattern_a, content)
gene_coords.extend(matches_a)
pattern_b=r"coding sequence =.*[actg\s\]]{1,}"
matches_b=re.findall(pattern_b, content)
coding_seq.extend(matches_b)


print(gene_coords)
print(coding_seq)

dict = {'gene-coordinates': gene_coords, 'coding-sequence': coding_seq} 
   
df = pd.DataFrame(dict)
   
#print(df)

# Specify the output file path
output_file = 'genome_coords_seq.tsv'
df.to_csv(output_file, sep='\t', index=False)
print(f"DataFrame successfully written as {output_file} \n {df}")


