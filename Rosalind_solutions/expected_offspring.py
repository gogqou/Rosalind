'''
Created on Oct 5, 2015
Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

@author: gogqou
'''
import numpy as np
import sys
def main():
    np.set_printoptions(threshold=1000, linewidth=1000, precision = 5, suppress = False)
    if len(sys.argv)<7:
        print 'provide number of each phenotype in a population:\n1.AA-AA\n2.AA-Aa\n3.AA-aa\n4.Aa-Aa\n5.Aa-aa\n6.aa-aa'
    if len(sys.argv)>7:
        print 'only used first six inputs'
    homhom = float(sys.argv[1])
    homhet = float(sys.argv[2])
    homrec = float(sys.argv[3])
    hethet = float(sys.argv[4])
    hetrec = float(sys.argv[5])
    recrec = float(sys.argv[6])
    
    total = float(2*(homhom+homhet+homrec+hethet+hetrec+recrec))
    dom = 2*homhom+2*homhet+2*homrec+2*3/float(4)*hethet+2*1/float(2)*hetrec
    expected = dom/total
    print expected
    return 1
if __name__ == '__main__':
    main()