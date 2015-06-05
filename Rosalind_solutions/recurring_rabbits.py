'''
Created on Jun 4, 2015
author: gogqou
'''


import sys
def recur(time, k, mapping):
    if time not in mapping.keys():
        #if I haven't calculated it (since I'm going top down)
        #I'll go back one step and use my definitions of the number of 
        # reproducing rabbits (a) and new rabbits (b) 
        # to calculate my current number of rabbits, and save that to the 
        # mapping
        c = recur(time-1, k, mapping)
        a = c[0]
        b = c[1]
        mapping[time] = [a+b, a*k]
    return mapping[time]
def main():
    
    if len(sys.argv)<3:
        print 'not enough inputs--please enter two numbers n = months and k = litter size'         
        sys.exit()
    elif len(sys.argv)>3:
        print 'too many inputs, only used first two'
    num_months = int(sys.argv[1])
    litter_size = int(sys.argv[2])
    rabbits = {}
    rabbits[1] = [0,1]
    #get a mapping that sets the initial conditions
    new_rabbits = recur(num_months, litter_size, rabbits)
    sum = new_rabbits[0]+new_rabbits[1]
    #total rabbits = new + reproducing rabbits
    print sum
    return sum
if __name__ == '__main__':
    main()