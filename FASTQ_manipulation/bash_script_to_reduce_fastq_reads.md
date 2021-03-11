
# This script is to reduce the number of reads from the original fastq to desired number 




* This is usually done on samples that are sequenced very deeply (more than desired),
* instances where you want to normalize the total reads before you start analyses.




***

##### Link to the tool github : https://github.com/lh3/seqtk

Seqtk is a fast and lightweight tool for processing sequences in the FASTA or FASTQ format. It seamlessly parses both FASTA and FASTQ files which can also be optionally compressed by gzip




* Before running the script make sure the scrip is executable 

  + on your terminal where */bash_script_to_reduce_fastq_reads.sh is :
    + run chmod u+x bash_script_to_reduce_fastq_reads.sh 
      (chmod u+x somefile will grant only the owner of that file execution permissions )
    
    + to run the script use - sh ./bash_script_to_reduce_fastq_reads.sh