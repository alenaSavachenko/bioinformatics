# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:42:01 2024

@author: Mijn-PC
"""

# Python program to demonstrate
# sys.argv

import re



origfilename ="bonafide.gb"
goodfilename ="nonred.loci.lst"



goodlist = {}
with open(goodfilename, 'r') as goodfile:
    for line in goodfile:
        goodlist[line.strip()] = 1

with open(origfilename, 'r') as origfile:
    content = origfile.read().split('\n//\n')
    for gendaten in content:
        match = re.match(r'^LOCUS +(\S+) .*', gendaten)
        if match:
            genname = match.group(1)
            if genname in goodlist:
                print(gendaten)
                with open('bonafide.f.nonred.gb', 'a') as f2:
                    f2.write( '//'+'\n'+gendaten+ '\n')
           
          
                
