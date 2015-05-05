'''
Created on May 5, 2015

@author: gogqou
'''
import sys
import fasta_io
def GC_content():
    inputfile = sys.argv[1]
    seqs_dict = fasta_io.fasta_io(inputfile)
    max_key = 'none'
    max_value = 0
    for key, value in seqs_dict.iteritems():
        count = 0
        for i in range(len(value)):
            if value[i] == 'C' or value[i]=='G':
                count = count +1
            gc = 100*float(count)/len(value)
        if gc>max_value:
            max_key= key
            max_value = gc
    print max_key
    print max_value
    return 1
if __name__ == '__main__':
    GC_content()