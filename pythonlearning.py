"""
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""


def capital_indexes(string):
    result = []
    i = 0
    for letter in string:
        if letter.isupper():
            result.append(i)
        i += 1
    return result


# better version
def capital_indexes2(string):
    result = []
    for i, letter in enumerate(string):
        if letter.isupper():
            result.append(i)
    return result


"""
Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""


def mid(word):
    if len(word) % 2 == 1:
        return word[len(word) // 2]
    else:
        return ""
