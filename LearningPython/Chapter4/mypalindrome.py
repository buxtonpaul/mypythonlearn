"""
Some information
"""


def palindrome1(source):
    """
    Function to return if a string is a palinfrome or not
    using list/string slicing
    """
    return source == source[::-1]


def palindrome2(source):
    """
    Function to return is a string is a palidrome using list reversal
    """
    seperated = list(source)  # seperate the string to a list
    seperated.reverse()     # reverse the list
    revstring = ''.join(seperated)  # convert to a string again
    return revstring == source

TESTCASES = ['abba', 'level', '101', 'fish', 'cheese']

for test in TESTCASES:
    if palindrome1(test) == True:
        print '%s is a Palindrome' % test
    else:
        print '%s is not a Palindrome' % test

RESULTS = map(palindrome2, TESTCASES)
for i in range(len(TESTCASES)):
    if RESULTS[i] == True:
        print '%s is a Palindrome' % TESTCASES[i]
    else:
        print '%s is not a Palindrome' % TESTCASES[i]
