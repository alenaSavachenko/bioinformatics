
# building new species

# before we build a new spies we have to format a string in gb file:
# LOCUS       OX457036.1 Lumbricus terrestris genome assembly, chromosome: 1_18743774-18745105   1332 bp  DNA
# this string  contains unique ID after the comma, and compiler can not access it. We have to split this string in order
# to give access to the unique ID ( 1_18743774-18745105).
# we wil use  python script to extarct unique ID, (this can be run in IDE)

#import re \
#with open("raw_data/bonafideET.gb") as f: \
   
#    data = f.read() \
     
# pattern = '(OX457036.1) Lumbricus terrestris genome assembly, chromosome: ([1-9_-]+\w+)' \

#result = re.sub( pattern, r'\1_\2' , data) \
# file_object = open('bonafide.unique.gb', 'w') \
# file_object.write(result) \
# file_object.close(  ) \
# f.close() 


# this wil replace LOCUS       OX457036.1 Lumbricus terrestris genome assembly, chromosome: 1_18743774-18745105   1332 bp  DNA
# throught  LOCUS       OX457036.1_1_50559-55310   4752 bp  DNA
# the new bonafide.unique.gb is in map data processing 

# soft link to  bonafide.gb

ln -s bonafide.unique.gb bonafide.gb

randomSplit.pl bonafide.gb 398

# this will create 2 files :  bonafide.gb.train, and   bonafide.gb.test
# First you need to check these two files that they are not null. The original set contains 1900 genes.
# sometimes you may find that the randomSplit program sends 0 genes to bonafide.gb.test   You have to chose 200 of them programmaticaly\

# If bonafide.gb.test is not null, you can proceed to the next step

mv bonafide.gb.test test.gb

#mv bonafide.gb.train train.gb

 etraining --species=wormET0  train.gb &> etrain.out


# you can find etreian.out in the map bonafide

tail -6 etrain.out | head -3

# this wil process output:

#tag:  511 (0.259)
#taa:  700 (0.354)
#tga:  764 (0.387)

# you need to change in the config map. wormET_parameters.cfg


augustus --species=wormET0  test.gb > test.out

# test.out gives evaluation of gene predicion, this file is in the map bonafide


#*******      Evaluation of gene prediction     *******

#---------------------------------------------\
#                 | sensitivity | specificity |
#---------------------------------------------|
#nucleotide level |       0.963 |       0.972 |
#---------------------------------------------/
#
#----------------------------------------------------------------------------------------------------------\
#           |  #pred |  #anno |      |    FP = false pos. |    FN = false neg. |             |             |
#          | total/ | total/ |   TP |--------------------|--------------------| sensitivity | specificity |
#           | unique | unique |      | part | ovlp | wrng | part | ovlp | wrng |             |             |
#----------------------------------------------------------------------------------------------------------|
#           |        |        |      |                 78 |                 87 |             |             |
#exon level |    389 |    398 |  311 | ------------------ | ------------------ |       0.781 |       0.799 |
#           |    389 |    398 |      |   56 |    6 |   16 |   56 |    6 |   25 |             |             |
#----------------------------------------------------------------------------------------------------------/
#
#----------------------------------------------------------------------------\
#transcript | #pred | #anno |   TP |   FP |   FN | sensitivity | specificity |
#----------------------------------------------------------------------------|
#gene level |   389 |   398 |  311 |   78 |   87 |       0.781 |       0.799 |
#----------------------------------------------------------------------------/
# total time: 31.2
# command line:
# augustus --species=wormET0 test.gb

