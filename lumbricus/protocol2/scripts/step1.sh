

# download transcriptome files


wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR108/049/ERR10851549/ERR10851549_1.fastq.gz
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR108/049/ERR10851549/ERR10851549_2.fastq.gz


# protein dataset comes from OrthoDB, Arthropoda  : https://bioinf.uni-greifswald.de/bioinf/partitioned_odb11/

# the protein database should be prepaired with ProtHints, if proteins are not preproccessed with ProtHints, you will get en error, running StartAlign.pl  Install ProtHints

# ProtHints installation
# Install     MCE::Mutex
# install    threads
# install     YAML
# install     Math::Utils
# install     GeneMarkES
# Download and extract the contents of the GeneMark-ES suite (versions 4.30 and up) into the ProtHint/dependencies/GeneMarkES folder. GeneMark-ES suite is available at http://exon.gatech.edu/GeneMark/license_download.cgi
#  To verify that GeneMark-ES is installed correctly, run the following command: ProtHint/dependencies/GeneMarkES/check_install.bash.

#install augustus
#install braker
