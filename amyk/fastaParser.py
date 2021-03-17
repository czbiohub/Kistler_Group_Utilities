#!/usr/bin/env/python

#name = fastaParser.py
#author = Amy Kistler
#date = 202010315

#usage = python fastaParser.py

#notes:
#this is VERY hacky script with a lot of hard coded components.
#all data are printed to screen.
#name of file to parse needs to be hard-coded below & you must also have that file in the wd.
#the slice index is hard-coded based on restriction enzyme cleavage position.


#import modules for fastaParser.py
import sys
import os
from Bio import SeqIO

#parse fasta file
for seq_record in SeqIO.parse('genscript_pUC57.fasta', 'fasta'): #hard-coded input file name
        print(seq_record.id)
        s=(str(seq_record.seq))
        print(len(seq_record))
        print(s)
        slice1 = s[:431] #hard-coded slice index based on restriction site cleavage position
        print(len(slice1)) #sanity check number of bp in slice 1
        print(slice1)
        print('')
        slice2 = s[431:] #hard-coded slice index based on restriction site cleavage position
        print(len(slice2)) #sanity check number of bp in slice 2
        print(slice2)
        l = len(slice1) + len(slice2) #sanity check that 2 fragments = entire plasmid
        print('')
        print(l)
