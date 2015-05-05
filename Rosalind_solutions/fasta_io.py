'''
Created on May 5, 2015

@author: gogqou
'''
from Bio import SeqIO
def fasta_io(file):
    seq_dict = {}
    for seq_record in SeqIO.parse(file, "fasta"):
        seq_dict[seq_record.id]=seq_record.seq
    return seq_dict