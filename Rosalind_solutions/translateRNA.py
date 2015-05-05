'''
Created on May 5, 2015
Problem

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
@author: gogqou
'''

import sys
import re
def parse_txt(txtfile):
    #read in txt file with >label + sequence afterwards
    dict = {}
    file = open(txtfile, 'r')
    for line in file:
        newline = line.rstrip()
        newline = newline.split(' ')
        dict[newline[0]] = newline[1]
    return dict
def translate():
    
    codonfile = sys.argv[1]
    RNA = sys.argv[2]
    codon_dict = parse_txt(codonfile)
    protein = ''
    for i in range(len(RNA)/3):
        AA = codon_dict[RNA[3*i:3*i+3]]
        protein = protein+AA
    print protein
    return 1
if __name__ == '__main__':
    translate()