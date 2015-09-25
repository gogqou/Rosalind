'''
Created on Sep 24, 2015

Build upon recurring rabbits:
rabbits die after a fixed number of months

Given: Positive integers n<=100 and m<=20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.


Added third input (litter size) for consistency with recurring_rabbits

@author: gogqou
'''
import sys

def recur(time, k, lifetime, mapping):
    if time not in mapping.keys():
        #if I haven't calculated it (since I'm going top down)
        #I'll go back one step and use my definitions of the number of 
        # reproducing rabbits (a, repro) and new rabbits (b, new_rabbits) 
        # to calculate my current number of rabbits, and save that to the 
        # mapping
        last_gen = recur(time-1, k, lifetime,mapping)
        repro = last_gen[0]
        new_rabbits = last_gen[1]
        #we incorporate the death by going back the length of the lifetime
        # and count how many newly born rabbits there are
        if time > lifetime:
            n_gen_ago = recur(time-lifetime, k, lifetime, mapping)
            death = n_gen_ago[1]
        else:
            death = 0
        #we account for death by subtracting the number that should die, based on going back 
        #the length of the lifetime
        #if time < lifetime, no death is expected
        mapping[time] = [repro+new_rabbits-death, repro*k]
    return mapping[time]
def main():
    
    if len(sys.argv)<4:
        print 'not enough inputs--please enter three numbers n = months, k = litter size, m = lifetime'         
        sys.exit()
    elif len(sys.argv)>4:
        print 'too many inputs, only used first three'
    num_months = int(sys.argv[1])
    litter_size = int(sys.argv[2])
    life_time = int(sys.argv[3])
    rabbits = {}
    rabbits[1] = [0,1]
    #get a mapping that sets the initial conditions
    new_rabbits = recur(num_months, litter_size,life_time, rabbits)
    sum = new_rabbits[0]+new_rabbits[1]
    #total rabbits = new + reproducing rabbits
    print sum
    return sum

if __name__ == '__main__':
    main()