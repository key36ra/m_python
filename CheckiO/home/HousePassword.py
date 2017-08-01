def checkio(data):

    re = False
    #d = [x for x in data.lower()]
    rstr = ["{}".format(x) for x in range(10)]
    # boolen must have "True" or "False"
    red = False
    for d in data:
        # data must have number.
        # "in" adjust to it, but "not in" sequence does nothing.
        if d in rstr:
            red = True
    if len(data) >= 10:
        if (data!=data.lower())&(data!=data.upper())&(red):
            re = True
    return re

# Clear solution.
"""
checkio = lambda s: not(
    len(s) < 10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
) 
"""

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
