# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:21:08 2024

@author: Mijn-PC
"""

import subprocess

with open('traingenes.lst', 'r') as f:
    patterns = f.read().splitlines()

with open('bonafide.gtf', 'r') as f:
    with open('bonafide.f.gtf', 'w') as out:
        for line in f:
            if any(pattern in line for pattern in patterns):
                out.write(line)
