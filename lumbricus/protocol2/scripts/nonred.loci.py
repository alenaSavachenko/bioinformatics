# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:22:15 2024

@author: Mijn-PC
"""

import subprocess

with open('nonred.lst', 'r') as f:
    patterns = f.read().splitlines()

with open('loci.lst', 'r') as f:
    loci = f.read().splitlines()

matched_loci = [locus.split('\t')[1] for locus in loci if any(pattern in locus for pattern in patterns)]

with open('nonred.loci.lst', 'w') as f:
    f.write('\n'.join(matched_loci))