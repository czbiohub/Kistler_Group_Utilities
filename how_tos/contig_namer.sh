## FILE FOR RENAMING CONTIG FILES!! 
for sample in `ls ./cycle_12/*cycle12.fasta`
  do
    dir="./"
    base=$(basename $sample "_contigs.cycle12.fasta")
      #subsample
            #turn files into .fq
    perl -p -e "s/^>/>${base}_/g" $sample > test.out; sed 's/[()\[]//g;s/\]//g' test.out > test2.out; sed 's/ /_/g' test2.out > ./contigs_named/${base}_contigs.out
  done
