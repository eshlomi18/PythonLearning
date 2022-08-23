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


"""
Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.

Write a function named online_count that takes one parameter.
The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
"""


def online_count(status):
    counter = 0
    for key, value in status.items():
        if value == "online":
            counter += 1
    return counter
