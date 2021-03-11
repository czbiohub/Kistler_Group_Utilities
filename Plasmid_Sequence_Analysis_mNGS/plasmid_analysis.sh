#!/bin/bash
#Sequences come in a folder named as the sample number 
#the first command is going to create directories analysis, docs, and sequences 
for dir in */
do
mkdir "$dir"/analysis "$dir"/docs "$dir"/sequences
done
#the next command would have to move all the sequences to the folder sequences 
find . -type f -name "*.gz" |while read file
do
mv $file ${file%/*}/sequences
done
find . -type f -name "*.fasta" |while read file
do
mv $file ${file%/*}/sequences
done
#we need a directory called index where the analysis will be directed, to create a directory use the following command
for dir in */analysis/
do
mkdir "$dir"/index
done
# the sequences provided from the sequencing team are in gunzip format. start with unzipping the .gz files
for f in */sequences/*R1_001.fastq.gz
do
f2=${f%R1_001.fastq.gz}R2_001.fastq.gz
gunzip $f $f2
done
# spin off the fastp command 
# flags: adapter recognition for PE reads is automatic, --poly_g_min_len and --poly_x_min_len is 5
ls */sequences/
for f in */sequences/*R1_001.fastq
do
f2=${f%R1_001.fastq}R2_001.fastq
fo=${f%.fastq}.fastp.fastq
f2o=${f2%.fastq}.fastp.fastq
#basename is for creating the report in individual directories 
basename=${f%R1_001.fastq}fastp_report
fastp -i $f -o $fo -I $f2 -O $f2o --poly_g_min_len 5 --poly_x_min_len 5 --html $basename.html --json $basename.json --detect_adapter_for_pe
#making terminal open the report in web broswer (MIGHT DELETE THIS IF WE HAVE MANY SAMPLES TO RUN; 1 REPORT IS ONE TAB)
#open $basename.html 
done
#the next step is to run the cdhit -dup to eliminate the duplicate files
#cd-hit-dup identifies duplicates (removes them) with specified criteria. "u" adds a condition which specifies the number of bases to use as a prefix to run cd hit. for example u 70 means that it will look for the first 70 bases as a length to look for duplicates and remove them. if it is a pair end read it will join two lengths (70 bases of each) and use the longer read to look for duplicates. any reads smaller than "u" will be filled with NNNs
#"e" specifies the tolerance level for mismatches, e= 0.05 means it can tolerate 5% dissimilarity in duplicate identification
for f in */sequences/*R1_001.fastp.fastq
do
f2=${f%R1_001.fastp.fastq}R2_001.fastp.fastq
fo=${f%.fastq}.dup.fastq
f2o=${f2%.fastq}.dup.fastq
basename=${f%R1_001.fastp.fastq}dup_report
cd-hit-dup -i $f -i2 $f2 -o $fo -o2 $f2o -e 0.05 -u 70 > $basename.txt  
done

#The next step is kick off bowite alignment with the provided variables
for f in */sequences/*_R1_001.fastq
do
basename=${f%_R1_001.fastq}
dir=$(dirname $f)
bowtie2-build -f $dir/*.fasta $basename
done

for f in */sequences/*_R1_001.fastp.dup.fastq
do
dir=$(dirname $f)
f2=${f%_R1_001.fastp.dup.fastq}_R2_001.fastp.dup.fastq
basename=${f%_R1_001.fastp.dup.fastq}
sambase=${f%_R1_001.fastp.dup.fastq}_bowtie_alignment_1000
report=${f%_R1_001.fastp.dup.fastq}_bowtie_report
bowtie2 -x $basename -q -1 $f -2 $f2 --very-sensitive-local -X 1000 -S $sambase.sam --no-unal --al-conc $sambase.fq 2> $report.txt
done


find */sequences -type f -name "*.bt2" |while read file
do
mv $file ${file%/*}/../analysis/index/	
done

find */sequences -type f -name "*report*" |while read file
do
mv $file ${file%/*}/../docs/	
done

for f in */analysis/index/*.sam
do
samtools view -S -b $f > ${f/.sam/.bam} 
done

for f in */analysis/index/*.bam
do
basename=${f%.bam}.sorted.bam
bedbasename=${basename%.sorted.bam}.sorted.bed
samtools sort $f -o $basename
bedtools bamtobed -i $basename > $bedbasename
done

for f in */sequences/*.fasta
do
samtools faidx $f 
done
find */sequences -type f -name "*fai" |while read file
do
mv $file ${file%/*}/../analysis/index/
done


for f in */analysis/index/*bowtie_alignment_1000.sorted.bed
do
dir=$(dirname $f)
genomefile="$dir/*.fasta.fai"
basename=${f%bowtie_alignment_1000.sorted.bed}1000.perBaseCov.tsv
bedtools genomecov -i $f -g $genomefile -d > $basename
done
for f in */analysis/index/*.tsv
do
csv=${f%.tsv}.csv
cat $f | tr "\t" "," > $csv
done


# for f in */sequences/*R1_001.fastp.dup.fastq
# do
# f2=${f%R1_001.fastp.dup.fastq}R2_001.fastp.dup.fastq
# basename= find . -type f -name "*.3.bt2" |${%.3.bt2}
# bowtie2 -x $basename -q -1 $f -2 $f2 --very-sensitive-local -X 1000 -S plasmidReference_1000.sam --no-unal --al-conc plasmidReference_1000.fq
# done
# find */sequences -type f -name "*.bt2" |while read file
# do
# mv $file ${file%/*}/../analysis/index
# done
# for dir in */analysis/index/
# do
# ls -lfh
# done
#kick-off bowtie alignment 



