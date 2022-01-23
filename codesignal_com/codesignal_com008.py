'''Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''


def solution(s1: str, s2: str):
    def recode(s):
        dict_result = dict()
        for letter in s:
            dict_result[letter] = dict_result.get(letter, 0) + 1
        return dict_result

    d1 = recode(s1)
    result = 0
    for letter, count in d1.items():
        result += min(count, s2.count(letter))
    return result


s1 = "aabcc"
s2 = "adcaa"
assert solution(s1, s2) == 3
