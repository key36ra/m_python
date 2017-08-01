def count_words(text, words):
    # "return" object must have any number or string.
    # this is the initial number.
    re = 0
    for i in words:
        # this search doesn't depend on isupper or islower.
        if i.lower() in text.lower():
            re += 1
    return re

# Clear solution.
"""
def count_words(text, words):
    return sum(w in text.lower() for w in words)
"""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
