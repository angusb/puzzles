"""
Generates all possible balanced parentheses strings up to the number of 
pairs specified.

Eg:

$ python balanced_parens.py 2
# [(), ()(), (())]
"""

import sys
from copy import deepcopy
from bisect import bisect_left

def _handle_insert(added_parens, elt):
    index = bisect_left(added_parens, elt)
    if len(added_parens) == index or elt != added_parens[index]:
        added_parens.insert(index, elt)

def recur(array, num_parens):
    if not num_parens:
        return array

    added_parens = deepcopy(array)
    for p in array:
        left = "()" + p
        outer = "(" + p + ")"
        right = p + "()"

        _handle_insert(added_parens, left)
        _handle_insert(added_parens, outer)
        _handle_insert(added_parens, right)

    num_parens += -1
    return recur(added_parens, num_parens)              

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    balanced = int(argv[1])
    print recur([""], balanced)

if __name__ == "__main__":
    main()
