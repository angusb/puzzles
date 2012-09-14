"""
Take a sequence of N numbers. We'll call the sequence a "Clean Chain of 
length N" if the sum of the first N - 1 numbers is evenly divisibly by 
the Nth number.

E.g.

First two chains are: 
- [2, 3, 5]
- [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

"""

import sys
from math import sqrt, floor

CHAINS = 3

def is_prime(x):
    """ Returns x if x is a prime, otherwise False. Note: only works 
    for x == 9 and x >= 11 """
    for i in xrange(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return x

def main(argv=None):
    if argv is None:
        argv = sys.argv

    primes = [2, 3]
    cnt = sum(primes)

    num_chains = 0
    x = 5
    while num_chains < CHAINS:
        if is_prime(x):
            primes.append(x)
            if cnt % x == 0:
                print primes # len(primes)
                num_chains += 1
            cnt += x
        x += 2

if __name__ == "__main__":
    main()
