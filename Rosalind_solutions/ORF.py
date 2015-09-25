'''
Created on Sep 25, 2015

@author: gogqou
'''
import transcribeDNA
import sys
import translateRNA_2
from Bio import SeqIO
def sliding_window(sequence, windowSize):
    seqdict={}
    proteins=[]
    start = []
    stop = []
    start_stop = []
    for i in range(len(sequence)-windowSize):
        #moving through the sequence with a windowSize as prescribed by user(3 for codons),
        #looking for the start codon sequence ATG
        
        seqdict[str(i)] = sequence[i:i+windowSize]
        if sequence[i:i+windowSize] == 'ATG':
            start.append(str(i))
            #once we've found the start codon, we take that reading frame and move forward 
            #one codon at a time til we find the stop codon
            stop.append(find_stop(sequence, i))
            #we then add this start, stop index pair to our running list 
            start_stop.append((start[-1], stop[-1]))
    print start_stop
    #for each start, stop combination, we take that sequence and transcribe, then translate
    for j in range(len(start_stop)):
        indices = start_stop[j]
        #start:stop indices
        seq = sequence[int(indices[0]):int(indices[1])+3] #the +3 gives us a stop codon
        #the translate function takes care to truncate the stop codon
        RNA=  transcribeDNA.transcribe(seq)
        protein = translateRNA_2.translate('/home/gogqou/Documents/codon.txt', RNA) 
        proteins.append(protein)     
    return proteins
def find_stop(sequence, start_index):
    #to find the stop codon immediately following the start codon we've identified 
    #at the start_index
    #we start 1 codon after, and increment at 3 nucleotides each time
    #if we find that the codon is in the list of stop codons
    #we return that index as the end of the sequence
    #otherwise, we keep looping
    for i in range(start_index+3, len(sequence)-start_index,3):
        if sequence[i:i+3] in ['TAG','TAA','TGA']:
            return i
        else:
            continue
    return len(sequence)
def main():
    input_file = sys.argv[1]
    record_dict = SeqIO.index(input_file, "fasta")
    for v in record_dict.itervalues():
        sequence = str(v.seq)
        proteins=sliding_window(sequence, 3)
        for i in range(len(proteins)):
            print proteins[i]
            
    return 1
if __name__ == '__main__':
    main()