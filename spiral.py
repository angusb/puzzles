"""
Prints out an arbitrary matrix in spiral order. Figuring it out is
definitely trickier than it seems. I would like to find a more
elegant solution in the future.

Note: requires a valid matrix.

E.g. spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) returns
[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

import sys

def spiral(matrix):
    xmin, ymin = 0, 1
    xmax, ymax = len(matrix[0]), len(matrix)

    result = []

    x, y, num = 0, 0, 0
    elts = len(matrix) * len(matrix[0])

    while num < elts:
        # Move right
        for x in range(xmin, xmax):
            result.append(matrix[y][x])
            num += 1
        xmax -= 1

        if num == elts: break

        # Move down
        for y in range(ymin, ymax):
            result.append(matrix[y][x])
            num += 1
        ymax -= 1

        if num == elts: break

        # Move left
        for x in reversed(range(xmin, xmax)):
            result.append(matrix[y][x])
            num += 1
        xmin += 1

        if num == elts: break

        # Move up
        for y in reversed(range(ymin, ymax)):
            result.append(matrix[y][x])
            num += 1
        ymin += 1

    return result

def main(argv=None):
    if argv is None:
        argv = sys.argv

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print spiral(matrix)

if __name__ == '__main__':
    main()
