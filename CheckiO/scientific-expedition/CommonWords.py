def checkio(first, second):
    # str is separated to word list.
    word_f = first.split(",")
    word_s = second.split(",")
    re = []
    # word in first appends to "re" list if the word's in second.
    for w in word_f:
        if w in word_s:
            re.append(w)
    # problem require sort.
    re.sort()
    # return string whose words connect with ",".
    return ",".join(re)


# Clear solution
"""
def checkio(first, second):
    return ','.join(sorted(set(first.split(',')) & set(second.split(','))))
    
"""
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
