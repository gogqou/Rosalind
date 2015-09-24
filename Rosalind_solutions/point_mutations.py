'''
Created on Jun 5, 2015
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

@author: gogqou
'''


import sys

def HammingDistance(string1='GAGCCTACTAACGGGAT', string2='CATCGTAATGACGGCCT'):
    dH = 0
    for i in range(len(string1)):
        if string1[i]==string2[i]:
            dH = dH + 0
            #print string1[i], string2[i]
        else:
            #print string1[i], string2[i]
            dH = dH + 1
    return dH

def main():
    if len(sys.argv)<3:
        print 'not enough inputs--please enter two strings to be compared'         
        sys.exit()
    elif len(sys.argv)>3:
        print 'too many inputs, only used first two'
    string_s = sys.argv[1]
    string_t = sys.argv[2]
    if len(string_s)!= len(string_t):
        print 'strings not same length, cannot compare'
        return 0
    print 'calculating Hamming Distance for: ',  string_s, 'and',  string_t
    dH = HammingDistance(string_s, string_t)
    print dH
    return dH
if __name__ == '__main__':
    main()