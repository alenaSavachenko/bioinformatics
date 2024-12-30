import re

txInGb3 = {}
txLocus = ""

with open("bonafideOrtho.gb.db") as file:
    for line in file:
        if re.search(r'LOCUS\s+(\S+)\s', line):
            txLocus = re.search(r'LOCUS\s+(\S+)\s', line).group(1)
        elif re.search(r'/gene="(\S+)"', line):
            gene = re.search(r'/gene="(\S+)"', line).group(1)
            txInGb3[gene] = txLocus

with open("loci.lst", "w") as output_file:
    for key in txInGb3.keys():
        output_file.write(f"{key}\t{txInGb3[key]}\n")
