#!/bin/bash

#this script is to reduce the fastq file size to desired reads 
#make sure your fastqs files are in the same directory as this script 

#this code chunk will create the directories needed for the execution and sorting of files 

for dir in ./
do
mkdir "$dir"/fastq "$dir"/fastq/seqtk_reduced_fastqs
done 

#this code chunk will look for the fastq files and move it to a bin called fastqs

find . -type f -name "*fastq.gz" |while read file
do
mv $file ${file%/*}/fastq/
done

#this code chunk will unzip teh fastq files which will be the input for seqtk

for f in ./fastq/*R1.fastq.gz
do
f2=${f%R1.fastq.gz}R2.fastq.gz
gunzip $f $f2
done

ls -lfh ./fastq/

#make sure the path to seqtk is edited to precise loaction 
#you can alternatively export the seqtk path permanently while insatlling seqtk
#make sure the -s value is same to keep the fastqs paired reads
#value for desired reads is an integer in the code line, here it is 10000 reads

for f in ./fastq/*R1.fastq 
do 
f2=${f%R1.fastq}R2.fastq 
~/Desktop/code/seqtk/seqtk sample -s100 $f 10000 > $f.reduced.fq 
~/Desktop/code/seqtk/seqtk sample -s100 $f2 10000 > $f2.reduced.fq 
done

#this code chunk is to move reduced fastqs to a separate folder 

find . -type f -name "*fq" |while read file
do
mv $file ${file%/*}/seqtk_reduced_fastqs/
done

ls -lfh ./fastq/seqtk_reduced_fastqs/

echo "script is executed, make sure to grep -c to confirm reduction in reads." 
