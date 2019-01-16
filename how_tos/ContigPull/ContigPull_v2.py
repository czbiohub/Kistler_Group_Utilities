#!/usr/bin/env python

"""ContigPull_v2.py"""

#author = Amy Kistler
#date = 20190114

#usage ContigPull.py contig_summary_file.csv ../sequences/contig_fasta_file.fasta tax_level tax_id
#to do - args for contig length option, tax level other than species; code in align length check

#importing python tools for script
import sys
import re
import string
from Bio import SeqIO
import pandas as pd
import numpy as np
import csv
import subprocess

#create node_list
node_list =[]

#summary of arguments provided at CLI
tax_id = sys.argv[4]

print('')
print('Summary of input information you provided:')

contig_summary_file = sys.argv[1]
print('Contig summary file = {0}'.format(contig_summary_file))

sample_id = contig_summary_file[0:11]
print('Sample = {0}'.format(sample_id))

tax_level = sys.argv[3]
#print('Taxonomy level to search = {0}'.format(tax_level)

#print('tax_id = {0}'.format(tax_id))
fastainfile = sys.argv[2]
contig_fasta_file = fastainfile.split("/")[2]
print('Contig fasta file = {0}'.format(contig_fasta_file))
print('')

#create outfiles for writing key data
tax_suffix = tax_level + "_" + tax_id + "_ContigNodeHits"

outfile1 = contig_fasta_file.rstrip("contigs.fasta") + tax_suffix + ".csv"
#print(outfile1)
node_listFile = open(outfile1, 'w')

outfile2 = contig_fasta_file.rstrip("contigs.fasta") + tax_suffix + ".fasta"
#print(outfile2)

outfile3 = "sample_listFile"
sample_info = open(outfile3,'w')
sample_info.write(contig_fasta_file)
sample_info.write("\n")
sample_info.write(tax_suffix)
sample_info.close()


#create pandas data frame from contig summary file
dfAll = pd.read_csv(contig_summary_file, index_col='contig_name')
#print(dfAll)
print('Pandas dataframe created from contig summary file. There are {0} rows'.format(len(dfAll)))

#create a pandas data frame for subset of contigs > 500bp long
dfAll500 = dfAll[(dfAll['contig_length'] > 500)]
#print(dfAll500)
print('{0} rows have contigs > 500bp'.format(len(dfAll500)))

#create new pandas dataframe for subset of contigs that align to taxID of interest at tax_level of interest
taxNR = 'NR.' + tax_level + "_taxid"
taxNT = 'NT.' + tax_level + "_taxid"
#print(taxNR)
#print(taxNT)

dfAll500taxNR = dfAll500[(dfAll500[taxNR].isin([tax_id]))]
#print(dfAll500taxNR)
print('{0} rows have NR matches to the taxID and tax level'.format((len(dfAll500taxNR)),(tax_id)))

dfAll500taxNT = dfAll500[(dfAll500[taxNT].isin([tax_id]))]
#print(dfAll500taxNT)
print('{0} rows have NT matches to the taxID and tax level'.format((len(dfAll500taxNT)),(tax_id)))

#create pandas data frame for contigs which show E-value <1e-3 for alignment to taxID at tax_level of interest
dfAll500taxNR1e3E = dfAll500taxNR[(dfAll500taxNR['NR.E-value'] < 0.001)]
#print(dfAll500taxNR1e3E)
print('{0} rows from the NR taxID matches show e-value < 1e-3'.format(len(dfAll500taxNR1e3E)))

dfAll500taxNT1e3E = dfAll500taxNT[(dfAll500taxNT['NT.E-value'] < 0.001)]
#print(dfAll500taxNT1e3E)
print('{0} rows from the NT taxID matches show e-value < 1e-3'.format(len(dfAll500taxNT1e3E)))

#compile index information (= contig_names) for contigs in final pandas data frame
NRnodes = dfAll500taxNR1e3E.index
NTnodes = dfAll500taxNT1e3E.index

for node in NRnodes:
    node_list.append(node)
for node in NTnodes:
    if node in node_list:
        pass
    else:
        node_list.append(node)
print('')
print('Here is the NR node list')
print(NRnodes)

print('')
print('Here is the NT node list')
print(NTnodes)

print('')
print('A total of {0} unique NR or NT alignments with e-values < 1e-3 were found for the taxID'.format(len(node_list)))
print('Here are the contig node ids that align to taxID {0}:'.format(tax_id))
print(node_list)

#write compiled contig_names to a file, 1 line per contig node ID
for n in node_list:
    node_listFile.write(n)
    node_listFile.write("\n")
node_listFile.close()


print('')
print('Node list has been written to {0}'.format(outfile1))
print('')
print('Now using node list to pull reads from {0}'.format(contig_fasta_file))

##incorporate # fasta reads that were pulled in this last statement
subprocess.call(['./contigPull.sh'])
print('Done! Contigs should be found in ../sequences/{0}'.format(outfile2))
