'''
Created on May 5, 2015

@author: gogqou
'''


import sys
import reverse_complement
def parse_fa_format(txtfile):
    #read in txt file with >label + sequence afterwards
    seq = ''
    file = open(txtfile, 'r')
    for line in file:
        if '>' not in line:
            lineagain = line.rstrip()
            seq = seq+lineagain
    return seq

def reverse_palindrome(dna, size):
    #check reverse complement for identity as we move through the sequence
    for i in range(len(dna)-size+1):
        substr = dna[i:i+size]
        rev = reverse_complement.reverse_complement(substr)
        if substr == rev:
            print i+1, size
    return 1
def main():
    file= sys.argv[1]
    seq= parse_fa_format(file)
    print seq
    for n in range(4,13):
        reverse_palindrome(seq,n)
    return 1
if __name__ == '__main__':
    main()