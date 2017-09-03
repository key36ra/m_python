def safe_pawns(pawns):
    # "safe pawn" means "the pawn is in attack area of another our pawn".
    a = [int(min(x)) for x in pawns if max(x)=="a"]
    b = [int(min(x)) for x in pawns if max(x)=="b"]
    c = [int(min(x)) for x in pawns if max(x)=="c"]
    d = [int(min(x)) for x in pawns if max(x)=="d"]
    e = [int(min(x)) for x in pawns if max(x)=="e"]
    f = [int(min(x)) for x in pawns if max(x)=="f"]
    g = [int(min(x)) for x in pawns if max(x)=="g"]
    h = [int(min(x)) for x in pawns if max(x)=="h"]
    count = 0
    for i in a:
        if i-1 in b:
            count += 1
    for i in b:
        if i-1 in a+c:
            count += 1
    for i in c:
        if i-1 in b+d:
            count += 1
    for i in d:
        if i-1 in c+e:
            count += 1
    for i in e:
        if i-1 in d+f:
            count += 1
    for i in f:
        if i-1 in e+g:
            count += 1
    for i in g:
        if i-1 in f+h:
            count += 1
    for i in h:
        if i-1 in g:
            count += 1
    return count
    

# Clear solution
"""
def safe_pawns(pawns):
    answer = 0
    for pawn in pawns :
        if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns : answer +=1
    return answer
"""


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
