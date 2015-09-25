'''
Created on Sep 25, 2015

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

AA to protein file used:
A 4
M 1
C 2
E 2
D 2
G 4
F 2
I 3
H 2
K 2
STOP 3
L 6
N 2
Q 2
P 4
S 6
R 6
T 4
W 1
V 4
Y 2
@author: gogqou
'''
import sys
def parse_txt(txtfile):
    #read in txt file with >label + sequence afterwards
    dict = {}
    file = open(txtfile, 'r')
    for line in file:
        newline = line.rstrip()
        newline = newline.split(' ')
        dict[newline[0]] = newline[1]
    return dict
def calc_AA_possibilities(proteinSeq, AA2prot_dict):
    AAposs= 1
    for i in range(len(proteinSeq)):
        AAposs = AAposs * int(AA2prot_dict[proteinSeq[i]])
    AAposs = AAposs* int(AA2prot_dict['STOP'])
    return AAposs
def main():
    if len(sys.argv)<3:
        print 'not enough inputs--please enter amino acid sequence and amino acid to protein file'         
        sys.exit()
    elif len(sys.argv)>3:
        print 'too many inputs, only used first two'
    AA = sys.argv[1]
    AA2prot = sys.argv[2]
    AA2prot_dict = parse_txt(AA2prot)
    #for k,v in AA2prot_dict.iteritems():
        #print k,v
    num_AA_possibilities = calc_AA_possibilities(AA, AA2prot_dict)
    print num_AA_possibilities
    print num_AA_possibilities%1000000
    return 1
if __name__ == '__main__':
    main()