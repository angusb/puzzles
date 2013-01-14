""" 
A MinStack implementation that returns the minimum element in O(1)
"""

import sys
from copy import deepcopy

class MinStackNaive:
    """
    A min-stack implementation that stores the minimum value seen for
    each value inserted.
    """

    class MinStackNode:
        def __init__(self, elt, min):
            self.elt = elt
            self.min = min

        def __repr__(self):
            return "<MinStackNode val: %s min: %s>" % (self.elt, self.min)

    def __init__(self):
        self.l = list()

    def push(self, *v):
        for i in range(len(v)):
            m = self.MinStackNode(v[i], min(v[i], self.min()))
            self.l.insert(0, m)

    def pop(self):
        v = self.l[0]
        del(self.l[0])
        return v

    def min(self):
        if not len(self.l):
            return sys.maxint
        else:
            return self.l[0].min

    def arr_repr(self):
        return deepcopy(self.l)


class MinStack():
    """
    A min-stack implementation that keeps track of the minimum values
    using an internal stack.

    Note: no better than MinStackNaive if the same minimum value is inserted
    repeatedly.
    """
    def __init__(self):
        self.l = list()
        self.minlist = list()

    def push(self, *v):
        for i in range(len(v)):
            self.l.insert(0, v[i])
            if v[i] <= self.min():
                self.minlist.insert(0, v[i])

    def pop(self):
        v = self.l[0]
        del(self.l[0])
        
        if v == self.min():
            del(self.minlist[0])

    def min(self):
        if not len(self.minlist):
            return sys.maxint
        else:
            return self.minlist[0]


def ugly_test(minstack):
    minstack.push(5, 4, 3, 1)

    # Ugly testing
    assert minstack.min() == 1
    minstack.pop()
    assert minstack.min() == 3
    minstack.push(-1)
    minstack.push(3)
    assert minstack.min() == -1
    minstack.push(-1)
    assert minstack.min() == -1
    minstack.pop()
    assert minstack.min() == -1
    minstack.pop()
    assert minstack.min() == -1

def main(argv=None):
    if argv is None:
        argv = sys.argv

    ugly_test(MinStackNaive())
    ugly_test(MinStack())

if __name__ == '__main__':
    main()
