'''
Created on Jun 4, 2015
    In 1202, Leonardo of Pisa (commonly known as Fibonacci) considered a mathematical exercise regarding the reproduction of a population of rabbits. He made the following simplifying assumptions about the population:

        The population begins in the first month with a pair of newborn rabbits.
        Rabbits reach reproductive age after one month.
        In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
        Exactly one month after two rabbits mate, they produce one male and one female rabbit.
        Rabbits never die or stop reproducing.

    Fibonacci's exercise was to calculate how many pairs of rabbits would remain in one year. We can see that in the second month, the first pair of rabbits reach reproductive age and mate. In the third month, another pair of rabbits is born, and we have two rabbit pairs; our first pair of rabbits mates again. In the fourth month, another pair of rabbits is born to the original pair, while the second pair reach maturity and mate (with three total pairs). The dynamics of the rabbit population are illustrated in Figure 1. After a year, the rabbit population boasts 144 pairs.

    Although Fibonacci's assumption of the rabbits' immortality may seem a bit farfetched, his model was not unrealistic for reproduction in a predator-free environment: European rabbits were introduced to Australia in the mid 19th Century, a place with no real indigenous predators for them. Within 50 years, the rabbits had already eradicated many plant species across the continent, leading to irreversible changes in the Australian ecosystem and turning much of its grasslands into eroded, practically uninhabitable parts of the modern Outback (see Figure 2). In this problem, we will use the simple idea of counting rabbits to introduce a new computational topic, which involves building up large solutions from smaller ones.

Problem


Given: Positive integers n <=40 and <=5.

Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
@author: gogqou
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