def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    cnt = 0
    c = 0
    for i in list(line):
        for j in range(len(line)):
            if list(line)[j] == i:
                c += 1
                if c > cnt:
                    cnt = c
                if j == len(line)-1:
                    c = 0
            else:
                c = 0
    return cnt

# Clear solution
"""
from itertools import groupby

def long_repeat(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)
"""
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
