'''
Created on May 4, 2015

@author: gogqou
'''
import sys
def reverse_complement(DNA):
    complement_DNA_dict = {}
    complement_DNA_dict ['A'] = 'T'
    complement_DNA_dict ['T'] = 'A'
    complement_DNA_dict ['C'] = 'G'
    complement_DNA_dict ['G'] = 'C'
    rev_comp = ''
    for i in range(len(DNA)):
        rev_comp = complement_DNA_dict[DNA[i]]+ rev_comp 
    return rev_comp
def main():
    DNA = sys.argv[1]
    print DNA
    rev_comp = reverse_complement(DNA)
    print rev_comp
    return 1
if __name__ == '__main__':
    main()