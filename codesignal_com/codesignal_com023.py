'''
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
Input/Output
[execution time limit] 4 seconds (py3)
[input] array.integer inputArray
Guaranteed constraints:
0 ≤ inputArray.length ≤ 104,
0 ≤ inputArray[i] ≤ 109.
[input] integer elemToReplace
Guaranteed constraints:
0 ≤ elemToReplace ≤ 109.
[input] integer substitutionElem
Guaranteed constraints:
0 ≤ substitutionElem ≤ 109.
[output] array.integer
'''


def solution(inputArray, elemToReplace, substitutionElem):
    return list(map(lambda x: substitutionElem if x==elemToReplace else x, inputArray))


inputArray = [1, 2, 1]
elemToReplace = 1
substitutionElem = 3
assert solution(inputArray, elemToReplace, substitutionElem) ==  [3, 2, 3]