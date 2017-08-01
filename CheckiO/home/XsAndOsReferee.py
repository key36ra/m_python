def checkio(game_result):
    re = "D"
    #game_vertical = [[game_result[i],game_result[i+1],game_result[i+2]].join() for i in range(3)]
    # horizontal or vertical rows evaluation.
    for i in range(3):
        if (game_result[i].count("O")==3)|([game_result[0][i],game_result[1][i],game_result[2][i]].count("O")==3):
            re = "O"
        elif (game_result[i].count("X")==3)|([game_result[0][i],game_result[1][i],game_result[2][i]].count("X")==3):
            re = "X"
    # diagonal rows evaluation.
    for x in ("O","X"):
        if ([game_result[0][0],game_result[1][1],game_result[2][2]].count(x)==3)|([game_result[0][2],game_result[1][1],game_result[2][0]].count(x)==3):
            re = x
    return re

# Clear solution.
"""
def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
​
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
"""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
