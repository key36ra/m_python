def checkio(text):
    # translate the all string to lower alphabet
    row = text.lower()
    # make alphabet list
    alp = "abcdefghijklmnopqrstuvwxyz"
    list = ""
    # use only alphabet of "text" in "alp"
    for x in row:
        if x in alp:
            list += x
    # initial data of return is fast alphabet of "text"
    re = min(list)
    for i in alp:
        # "s.count(i)" is the count number of i in s as string.
        if list.count(i) == max(list.count(a) for a in list):
            re = i
            break
    return re

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
