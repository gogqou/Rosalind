'''
Created on Sep 24, 2015

 graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph O_k in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s=/=t; we demand s=/=t to prevent directed loops in the overlap graph (although directed cycles may be present).


Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

@author: gogqou
'''

from Bio import SeqIO
import sys
import difflib
import itertools
def overlap_graphs(seq_dict):
    #takes input of a dictionary of sequences (based on the SeqIO index format
    #where both sequence id and name are attributes of the value
    #and the key is the name again
    overlapGraph = []
    for k,k2 in itertools.combinations(seq_dict, 2):
        v =seq_dict [k]
        v2=seq_dict[k2]
        s1 = str(v.seq[:3])
        s2 = str(v2.seq[-3:])
        if s1==s2:
            #can choose to make it a directed graph two ways
            #in my check_overlap, I'm checking if the prefix of s1 matches
            #the suffix of s2
            #so if it works, I actually need to reverse the name listing
            #to make it a directed graph
            #or I could've changed which suffix and prefix I was checking
            overlapGraph.append((v2.name, v.name))
        s1 = str(v2.seq[:3])
        s2 = str(v.seq[-3:])    
        if s1==s2:
            overlapGraph.append((v.name, v2.name))
    return overlapGraph

def main():
    if len(sys.argv)<2:
        print 'not enough inputs--please insert file source'         
        sys.exit()
    elif len(sys.argv)>2:
        print 'too many inputs, only used first'
    input_file = sys.argv[1]
    handle = open(input_file, "rU")
    #fasta_records = list(SeqIO.parse(handle, "fasta"))
    #for larger record sets, SeqIO index is better for memory management
    record_dict = SeqIO.index(input_file, "fasta")
    handle.close()
    ovGraph= list(set(overlap_graphs(record_dict)))
    for i in range(len(ovGraph)):
        print ovGraph[i][0] + ' ' + ovGraph[i][1]
        #print record_dict[ovGraph[i][0]].seq
        #print record_dict[ovGraph[i][1]].seq
    return 1
if __name__ == '__main__':
    main()