'''
Created on May 5, 2015

@author: gogqou
'''
from Bio import SeqIO
def fasta_io(file):
    
    for seq_record in SeqIO.parse("file", "fasta"):
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))
    seqs = []
    return seqs