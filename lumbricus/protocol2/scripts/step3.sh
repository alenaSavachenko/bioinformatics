

# get Blast rest Api

wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/

# set  path

export PATH=$PATH:$HOME/ncbi-blast-2.16.0+

#this script from protocol 6 is replaced thought create_train_list.py, run in python IDE
# this lines code from protocol are replaced:
#cat bonafide.gb | perl -ne ’if(m/\/gene=\"(\S+)\"/){ \
#print "\"".$1."\"\n";}’ | sort -u > traingenes.lst
#
#  this step creates traingenes.lst, see map data-processing, redudancy

# than create bonafide.f.gtf. in a python IDE instead of perl,see createbonafidef.py., for the output see map   redudancy  data-processing

# Convert training gene structure gtf file and FASTA file to a FASTA file containing protein sequence with following commnado

gtf2aa.pl genome.fa bonafide.f.gtf prot.aa


# see prot.aa file in redudancy data processing map

# blast aminoacids

aa2nonred.pl prot.aa prot.nr.aa

# file prot.nr.aa, see in map redudancy data processing

# this script form protocol 6 is replaced thought, grep -oE '(OX457036[A-Za-z1-9._]{1,})\w+'  prot.nr.aa > nonred.lst

# this line from protocol 6 is replaced:
#  grep ">" prot.nr.aa | perl -pe ’s/>//’ > nonred.lst

grep -oE '(OX457036[A-Za-z1-9._]{1,})\w+'  prot.nr.aa > nonred.lst

# this produces nonredundant subset of genes, see map redudancy, nonred.lst


# this script of protocl 6:
cat bonafide.gb | perl -ne ’
if ( $_ =~ m/LOCUS\s+(\S+)\s/ ) {
$txLocus = $1;
} elsif ( $_ =~ m/\/gene=\"(\S+)\"/ ) {
$txInGb3{$1} = $txLocus
}
if( eof() ) {
foreach ( keys %txInGb3 ) {
print "$_\t$txInGb3{$_}\n";
}
}’ > loci.lst

# is replaced thought  locilist.py  and nonred.loci.py, schould be run in python IDE
# this produces loci.lst and  nonred.loci.lst, see map reduancy


#this script from protocol 6
 filterGenesIn.pl nonred.loci.lst bonafide.gb > bonafide.f.gb
# captures only the last Locus, while there are 600 genes on 
# list. 
#  it is necessary to convert this into a loop, 
#that would grab all 600 genes, not just the last one on the list. 

# the modified file is : bonafide.nonred.f.py, run on python IDE
# aftter run the script. it is necessary to delete the first  //   of the file from the first line in the gb file
#  it prouces file  bonafide.f.gb  with 600 genes, see map reduancy
# sometimes you can get complainig of non-genebank format, than you have to fix it with text editor, add extra whitespace and doubleslash after each locus
#this can be done automatically with a text editor, supporting regex, such as notepad++
# Regex for Locus:
#   (LOCUS.*OX457036[A-Za-z1-9._-]{1,}.*)


# the next step is creating  new model (species), Creating new model wil be descrbed in protocol 1 
