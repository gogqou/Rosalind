'''
Created on Sep 25, 2015

@author: gogqou
'''
import transcribeDNA
import translateRNA_2
def sliding_window(sequence, windowSize):
    seqdict = {}
    start = []
    stop = []
    start_stop = []
    for i in range(len(sequence)-windowSize):
        seqdict[str(i)] = sequence[i:i+windowSize]
        if sequence[i:i+windowSize] == 'ATG':
            start.append(str(i))
            print sequence[i:i+3]
            stop.append(find_stop(sequence, i))
            start_stop.append((start[-1], stop[-1]))
    for j in range(len(start_stop)):
        indices = start_stop[j]
        print indices
        seq = sequence[int(indices[0]):int(indices[1])+3]
        print seq
        RNA=  transcribeDNA.transcribe(seq)
        print RNA
        protein = translateRNA_2.translate('/home/gogqou/Documents/codon.txt', RNA) 
        print protein     
    return seqdict
def find_stop(sequence, start_index):
    for i in range(start_index+3, len(sequence)-start_index,3):
        print i
        if sequence[i:i+3] in ['TAG','TAA','TGA']:
            return i
        else:
            continue
    return len(sequence)
def main():
    
    sequence = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
    seqdict=sliding_window(sequence, 3)
    return 1
if __name__ == '__main__':
    main()