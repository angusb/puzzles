"""
Given a tuple (inputted as a string) output all possible combinations 
with '*' marking empty locations.

My attempt is to make this as functional as possile. Not quite there yet.

Eg:

$ python combs.py "(a, b, c)"
# [('a', 'b', 'c'), ('*', 'b', 'c'), ('*', '*', 'c'), ('*', '*', '*'), 
#  ('*', 'b', '*'), ('a', '*', 'c'), ('a', '*', '*'), ('a', 'b', '*')]
"""

import sys
from copy import deepcopy
from itertools import repeat

def get_combs(dest, source, combs):
    """
    Produce all possible combinations of source and store them in combs.
    Each combination is an array.
    """
    combs.append(dest)

    for i in range(len(source)):
        dest.append(source[0])
        del(source[0])
        get_combs(deepcopy(dest), deepcopy(source), combs)
        dest.pop()

def format(index_array, str_arr):
    """
    For each index within index_array, replace the corresponding index
    of str_arr with a '*'. TODO: more elegant
    """
    str_arr = deepcopy(str_arr)
    for i in index_array:
        str_arr[i] = '*'
    return tuple(str_arr)

def main(argv=None):
    if argv is None:
        argv = sys.argv 

    combs = []
    array = list(filter(lambda x: x not in ' ),(', argv[1])) # Array of chars
    get_combs([], range(len(array)), combs)
    
    print map(format, combs, repeat(array, len(combs)))

if __name__ == "__main__":
    main()
