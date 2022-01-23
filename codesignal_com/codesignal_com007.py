'''Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
'''


def solution(inputArray):
    max_length = 0
    for x in inputArray:
        max_length = max(max_length, len(x))
    return list(filter(lambda x: len(x) == max_length, inputArray))


inputArray = ["aba", "aa", "ad", "vcd", "aba"]
assert solution(inputArray) == ["aba", "vcd", "aba"]
