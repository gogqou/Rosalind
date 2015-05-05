'''
Created on May 4, 2015

@author: gogqou
'''
import sys
def count(input):
    alphabet_dictionary = {}
    for i in range(len(input)):
        if input[i] in alphabet_dictionary.keys():
            alphabet_dictionary[input[i]]=alphabet_dictionary[input[i]] +1
        else: 
            alphabet_dictionary[input[i]]= 1
    return alphabet_dictionary
def print_results(alphabet_dictionary):
    for key, value in alphabet_dictionary.iteritems():
        print key,value
    return 1
def main():
    DNA = sys.argv[1]
    print DNA
    alpha_dict = count(DNA)
    print_results(alpha_dict)
    return 1
if __name__ == '__main__':
    main()