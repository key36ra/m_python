def checkio(text):
    list = text.lower()
    alp = "abcdefghijklmnopqrstuvwxyz"
    # We must input the initial value to name.
    count = {name:0 for name in alp}
    for i in alp:
        # "if" is called only one time.
        if i in list:
            count[i] += 1
    # "max" method doesn't mean maximum number but mean last word in dict.
    if max(count.values()):
        for i in alp:
            if count[i] == max(count.values()):
                return i
    else:
        return 'e'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
