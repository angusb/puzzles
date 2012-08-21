"""
Finds all triples in an array that sum to 0.

Eg.

$ python triples.py "5, 4, 0, -5, -3, -2, -2, 2"
# [(-5, 0, 5), (-3, -2, 5), (-3, -2, 5), (-2, -2, 4), (-2, 0, 2), (-2, 0, 2)]
"""

import sys

def get_triples(array):
    if len(array) < 3:
        return "The array has to be of length >= 3"

    array.sort() # In place sort

    lower = 0
    upper = len(array) - 1
    result = []

    while(lower < upper):
        l_iter = lower + 1
        u_iter = upper

        while l_iter < u_iter:
            tmp = array[lower] + array[l_iter] + array[u_iter]
            if tmp == 0:
                result.append((array[lower], array[l_iter], array[u_iter]))
            if tmp <= 0:
                l_iter += 1
            else:
                u_iter -= 1

        lower += 1

    return result

def main(argv=None):
    if argv is None:
        argv = sys.argv

    string_list = argv[1].split(',')
    array = map(lambda x: int(x), string_list)

    print get_triples(array)

if __name__ == "__main__":
    main()
