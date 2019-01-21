#!/usr/bin/env python

"""ContigPull_v3.py"""
#For pulling contigs for a specific tax level & identifier from a given sample that has been analyzed in IDseq.
#User provides IDseq sampleID_contigs_summary_file.csv, sampleID_contigs.fasta file, the tax level (e.g., family, genus, species) and NCBI tax id of interest.
#The script will push sampleID_contigs_summary_file.csv to pandas dataframe, then generate a list of contig NODE ids that correspond to contigs that are at least 300bp long, with < 1e2 evalue and and > 50% contig query length alignments to NT and NR hits for user-specified tax id.
#The NODE id list is fed to the shell script contigPull.sh which writes fasta records for each item in the NODE list file to a batch fasta file.
#current hard-coded defaults = minimum contig length = 300bp; maximum alignment e-value = 1e-2; minimum %query alighment = 50%

#note: to run script - need to have 2 directories: analysis and sequences. sampleID_contig_summary_file.csv, ContigPull_v3.py and contigPull.sh need to be in analysis directory.
#sampleID_contigs.fasta file for sample needs to be in sequences directoryself.

#author = Amy Kistler
#date = 20190118

#usage: python ContigPull_v3.py sampleID_contig_summary_file.csv ../sequences/sampleID_contig_fasta_file.fasta tax_level tax_id
#example: python ContigPull_v3.py CMS001_035_Ra_S20_contigs_summary.csv ../sequences/CMS001_035_Ra_S20_contigs.fasta family 5654
#expected output:
 ##stdout = realtime progress are printed to screen - summary of arguments for inputs, statistics re pandas dataframe filtering, details on node list are printed to screen.
 ##analysis/sample_listFile = text file with 2 lines = line 1 = contigs.fasta input filename, line 2 = tax_suffix
 ##analysis/*_contigs_tax_level_tax_id_ContigNodeHits.txt = line separated NODE ids for contigs which meet user-specified criteria for sequence pulling.
 ##sequences/*_contigs_tax_level_tax_id_ContigNodeHits.fasta = batch fasta file of contigs that meet user-specified criteria for pulling.



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


print('')
print('Summary of input information you provided:')

contig_summary_file = sys.argv[1]
print('Contig summary file = {0}'.format(contig_summary_file))

sample_id = contig_summary_file[0:11]
print('Sample = {0}'.format(sample_id))

tax_level = sys.argv[3]
tax_id = sys.argv[4]
print('tax_level = {0}'.format(tax_level))
print('tax_id = {0}'.format(tax_id))

fastainfile = sys.argv[2]
contig_fasta_file = fastainfile.split("/")[2]
print('Contig fasta file = {0}'.format(contig_fasta_file))
print('')

#create outfiles for writing key data
tax_suffix = tax_level + "_" + tax_id + "_ContigNodeHits"

outfile1 = contig_fasta_file.rstrip("contigs.fasta") + tax_suffix + ".txt"
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
dfAll300 = dfAll[(dfAll['contig_length'] > 300)]
#print(dfAll300)
print('{0} rows have contigs > 300bp'.format(len(dfAll300)))

#create new pandas dataframe for subset of contigs that align to taxID of interest at tax_level of interest
taxNR = 'NR.' + tax_level + "_taxid"
taxNT = 'NT.' + tax_level + "_taxid"
print(taxNR)
print(taxNT)

dfAll300taxNR = dfAll300[(dfAll300[taxNR].isin([tax_id]))]
#print(dfAll300taxNR)
print('{0} rows have NR matches to {1} and tax level'.format((len(dfAll300taxNR)),(tax_id)))

dfAll300taxNT = dfAll300[(dfAll300[taxNT].isin([tax_id]))]
#print(dfAll300taxNT)
print('{0} rows have NT matches to the {1} and tax level'.format((len(dfAll300taxNT)),(tax_id)))

#create pandas data frame for contigs which show E-value <1e-3 for alignment to taxID at tax_level of interest
dfAll300taxNR1e2E = dfAll300taxNR[(dfAll300taxNR['NR.E-value'] < 0.01)]
#print(dfAll300taxNR1e3E)
print('{0} rows from the NR taxID matches show e-value < 1e-2'.format(len(dfAll300taxNR1e2E)))

dfAll300taxNT1e2E = dfAll300taxNT[(dfAll300taxNT['NT.E-value'] < 0.01)]
#print(dfAll300taxNT1e3E)
print('{0} rows from the NT taxID matches show e-value < 1e-2'.format(len(dfAll300taxNT1e2E)))

dfAll300taxNR1e2E['NR.PercentQueryAligned'] = (dfAll300taxNR1e2E['NR.Alignment Length']*3)/dfAll300taxNR1e2E['contig_length']
#print(dfAll300taxNR1e2E.head())

dfAll300taxNT1e2E['NT.PercentQueryAligned'] = dfAll300taxNT1e2E['NT.Alignment Length']/dfAll300taxNT1e2E['contig_length']
#print(dfAll300taxNT1e2E.head())

dfAll300taxNR1e2E50p = dfAll300taxNR1e2E[(dfAll300taxNR1e2E['NR.PercentQueryAligned'] > 0.5)]
print('{0} rows from the NR taxID matches show alignments > 50% query contig length'.format(len(dfAll300taxNR1e2E50p)))

dfAll300taxNT1e2E50p = dfAll300taxNT1e2E[(dfAll300taxNT1e2E['NT.PercentQueryAligned'] > 0.5)]
print('{0} rows from the NT taxID matches show alignments > 50% query contig length'.format(len(dfAll300taxNT1e2E50p)))

#compile index information (= contig_names) for contigs in final pandas data frame
NRnodes = dfAll300taxNR1e2E50p.index
NTnodes = dfAll300taxNT1e2E50p.index

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
print('A total of {0} unique NR or NT alignments that met all criteria were found for the taxID'.format(len(node_list)))
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
print('Now using node list to pull contig records from {0}'.format(contig_fasta_file))

##incorporate # fasta reads that were pulled in this last statement
subprocess.call(['./contigPull.sh'])
print('Done! Contigs should be found in ../sequences/{0}'.format(outfile2))
