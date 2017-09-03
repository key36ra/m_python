from math import *

def checkio(a, b, c):
    # input initial data for non-triangle.
    A,B,C = (0,0,0)
    re = []
    # try culculation for three angle as radian.
    try:
        s = (a+b+c)/2
        S = sqrt(s*(s-a)*(s-b)*(s-c))        
        if a>=b and a>=c and a<b+c:
            h = 2*S/a
            B,C = (asin(h/c),asin(h/b))
            A = pi-B-C
        elif b>=c and b>=a and b<c+a:
            h = 2*S/b
            C,A = (asin(h/a),asin(h/c))
            B = pi-C-A
        elif c>=a and c>=b and c<a+b:
            h = 2*S/c
            A,B = (asin(h/b),asin(h/a))
            C = pi-A-B
    except:
        pass
    # translate radian to integer degrees, and make list.
    for x in (degrees(A),degrees(B),degrees(C)):
        if x >= (ceil(x)+floor(x))/2:
            x = ceil(x)
        else:
            x = floor(x)
        re.append(x)
    # the angle list must be sorted.
    return sorted(re)


# Clear solution
"""
def checkio(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return [0, 0, 0]
    find_angle = lambda s1, s2, so: int(round(
        degrees(acos((s1 ** 2 + s2 ** 2 - so ** 2) / (2 * s1 * s2))), 0))
    return sorted([find_angle(a, b, c), find_angle(a, c, b), find_angle(b, c, a)])
"""


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
