'''
Created on Oct 5, 2015

A matrix is a rectangular table of values divided into rows and columns. An $m \times n$ matrix has $m$ rows and $n$ columns. Given a matrix $A$, we write $A_{i, j}$ to indicate the value found at the intersection of row $i$ and column $j$.

Say that we have a collection of DNA strings, all having the same length $n$. Their profile matrix is a $4 \times n$ matrix $P$ in which $P_{1,j}$ represents the number of times that 'A' occurs in the $j$th position of one of the strings, $P_{2,j}$ represents the number of times that C occurs in the $j$th position, and so on (see below).

A consensus string $c$ is a string of length $n$ formed from our collection by taking the most common symbol at each position; the $j$th symbol of $c$ therefore corresponds to the symbol having the maximum value in the $j$-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.





Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)



@author: gogqou
'''

import sys
from Bio import SeqIO
import numpy as np
def make_profile(DNA_dictionary, string_length):
    consensusSeq = ''
    A = np.zeros([string_length,1])
    C = np.zeros([string_length,1])
    G = np.zeros([string_length,1])
    T = np.zeros([string_length,1])
    #iterate through each position in the DNA string
    for i in range(string_length):
        #iterate through each entry in the list of DNA strings
        for v in DNA_dictionary.itervalues():
            if v.seq[i] == 'A':
                A[i] = A[i]+1
            elif v.seq[i] == 'G':
                G[i] = G[i]+1
            elif v.seq[i] == 'T':
                T[i] = T[i]+1
            elif v.seq[i] == 'C':
                C[i] = C[i]+1
            else:
                print 'non triggered'
        current= [A[i], C[i], G[i], T[i]] 
        #put all the current counts in a list
        #find the index of the maximum value
        max_index = np.argmax(current)
        #iterate through the possibilities to assign the consensus 
        #nucleotide for this position
        if max_index ==0:
            consensusSeq=consensusSeq+'A'
        elif max_index ==1:
            consensusSeq=consensusSeq+'C'
        elif max_index ==2:
            consensusSeq=consensusSeq+'G'
        elif max_index ==3:
            consensusSeq=consensusSeq+'T'
          
    return consensusSeq, A.transpose(),C.transpose(),G.transpose(),T.transpose()
def main():
    np.set_printoptions(threshold=1000, linewidth=1000, precision = 5, suppress = False)
    if len(sys.argv)<2:
        print 'provide file location of input fasta file of DNA strings'
    if len(sys.argv)>2:
        print 'only used first input'
    input_file = sys.argv[1]
    #put all the DNA strings into a dictionary using BioPython
    record_dict = SeqIO.index(input_file, "fasta")
    first_key =list(record_dict.keys())[0]
    #figure out how long the DNA string is
    DNAlength= len( record_dict[first_key].seq)
    [consensus, A,C,G,T] = make_profile(record_dict, DNAlength)
    
    print consensus
    print 'A: ', A.astype(int)
    print 'C: ', C.astype(int)
    print 'G: ', G.astype(int)
    print 'T: ', T.astype(int)
    return 1
if __name__ == '__main__':
    main()