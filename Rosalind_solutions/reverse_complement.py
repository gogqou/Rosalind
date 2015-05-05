'''
Created on May 4, 2015

@author: gogqou
'''
import sys
def reverse_complement(DNA):
    #generate a dictionary that helps with generating a complement
    #assign complementarity to each nucleotide
    complement_DNA_dict = {}
    complement_DNA_dict ['A'] = 'T'
    complement_DNA_dict ['T'] = 'A'
    complement_DNA_dict ['C'] = 'G'
    complement_DNA_dict ['G'] = 'C'
    #initialize an empty string for our reverse complement
    rev_comp = ''
    for i in range(len(DNA)):
        #as we cycle through 'DNA', we add each next complement to the beginning of 'rev_comp' 
        #to get the reverse complement
        rev_comp = complement_DNA_dict[DNA[i]]+ rev_comp 
    return rev_comp
def main():
    #input should be the DNA seq you want to transcribe
    if len(sys.argv)<2:
        print 'please enter DNA sequence to transcribe'         
        sys.exit()
    elif len(sys.argv)>2:
        print 'too many inputs, only used first entry'
    DNA = sys.argv[1]
    rev_comp = reverse_complement(DNA)
    print rev_comp
    return 1
if __name__ == '__main__':
    main()