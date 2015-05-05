'''
Created on May 4, 2015

@author: gogqou
'''
import sys
def transcribe(DNA):
    transcribe_dict = {}
    RNA = ''
    for i in range(len(DNA)):
        if DNA[i] == 'T':
            RNA= RNA + 'U'
        else: 
            RNA= RNA + DNA[i]       
    return RNA
def main():
    DNA = sys.argv[1]
    print DNA
    RNA = transcribe(DNA)
    print RNA
    return 1
if __name__ == '__main__':
    main()