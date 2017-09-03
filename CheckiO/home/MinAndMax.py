def min(*args, **kwargs):
    # "*args" means only "value", and return the tupl.
    # "**kwargs" means "key=value", and return the dict.
    # "lambda argument: expression" returns "def lambda(argument): return expression".
    #key = kwargs.get("key", None)
    re = None
    ar = args
    if kwargs:
        ar = kwargs["key"](ar)
    for i in range(9):
        if i in ar:
            re = i
            break
            
    print(ar)


def max(*args, **kwargs):
    #key = kwargs.get("key", None)
    # we can't use "max()" function because same function name raise RecursionException.
    re = None
    ar = args
    if kwargs:
        ar = kwargs["key"](ar)
    for i in range(9,0,-1):
        if i in ar:
            re = i
            break
            
    print(ar)


max(3,2)
min(3,2)
max([1,2,0,3,4])
min("hello")
max(2.2, 5.6, 5.9, key=int)



"""
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
"""