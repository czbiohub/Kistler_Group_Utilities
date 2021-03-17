 #!/usr/bin/env python

#name = GBreader.py
#author = Amy Kistler
#date = 20191116

#usage: python GBreader.py

#notes:
#this is a quick biopython script i wrote to parse fasta defline and  sequence data from genbank files.
#input genbank file (suffix ".gb") must be in the same working directory where you call the script.
#input genbank file name is currently hard-coded.
#data are simply written to screen -- I think I had some troubles writing to file when I put this together .


#import modules
from Bio import SeqIO
import os
import sys

#open file for writing out fasta record
f = open('GE_CMVE1.fasta', 'w+')

#open input gbank file you want to parse
record = SeqIO.read('1_ge-cmv-e1_plasmid_e1_pcdn.gb','genbank')
print(record.name)
print(record.seq)
#print(('{} {} \n'.format('>',record.id))
#print(record.seq)
#f.write(record.name)
#f.write(record.seq)
#f.close()

