'''
Codewriting

300

Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

Palindrome
A string that doesn't changed when reversed (it reads the same backward and forward).

Examples:

"eye" is a palindrome
"noon" is a palindrome
"decaf faced" is a palindrome
"taco cat" is not a palindrome (backwards it spells "tac ocat")
"racecars" is not a palindrome (backwards it spells "sracecar")
'''


def solution(inputString):
    set1 = set(list(inputString))
    res2 = list(filter(lambda x: inputString.count(x) % 2 != 0, set1))
    if len(res2) > 1:
        return False
    return True


inputString = "aabb"
assert solution(inputString) is True

inputString = "abbcabb"
assert solution(inputString) is True

inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
assert solution(inputString) is False

inputString = "abcd"
assert solution(inputString) is False
