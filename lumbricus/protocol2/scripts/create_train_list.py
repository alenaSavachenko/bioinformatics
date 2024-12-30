# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:33:07 2024

@author: Mijn-PC
"""

import re
import subprocess

# Read from the file
with open('bonafide.locus.gb', 'r') as file:
    content = file.readlines()

# Extract unique gene names
gene_names = set()
for line in content:
    match = re.search(r'/gene="(\S+)"', line)
    if match:
        gene_names.add(match.group(1))

# Sort and write to the output file
with open('traingenes.lst', 'w') as output_file:
    for gene in sorted(gene_names):
        output_file.write(f'"{gene}"\n')