'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; 
i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.
'''


def solution(inputString):
    alphabet = "abcdefghijklmnopqrstuvwxyza"
    result = ""
    for x in inputString:
        result += alphabet[alphabet.find(x)+1]
    return result


assert solution("crazy") == "dsbaz"
assert solution("abcz") == "bcda"
# assert solution() ==
# assert solution() ==
