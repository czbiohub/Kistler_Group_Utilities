#!/bin/bash
{ read -r var1 ; read -r var2 ; } < sample_listFile;
#echo "$var1 $var2"
cat ../sequences/$var1 | seqkit grep -f $(basename $var1 contigs.fasta)$var2.txt  > ../sequences/$(basename $var1 contigs.fasta)$var2.fasta
#done <sample_listFile 3<taxID_list

