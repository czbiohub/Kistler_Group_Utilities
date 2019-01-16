#!/bin/bash
{ read -r var1 ; read -r var2 ; } < sample_listFile;
#echo "$var1 $var2"


#while read -r ONE; 
#do 
    #read -r TWO
    #echo "ONE: $ONE TWO: $RWO"
#done < sample_listFile



#while read LINE; do echo "$LINE"; done < sample_listFile
#while IFS= read -r lineA && IFS= read -r lineB <&3; do
    #echo "$lineA"; echo "$lineB"
cat ../sequences/$var1 | seqkit grep -f $(basename $var1 contigs.fasta)$var2.csv  > ../sequences/$(basename $var1 contigs.fasta)$var2.fasta
#done <sample_listFile 3<taxID_list

