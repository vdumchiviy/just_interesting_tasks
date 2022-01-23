'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be solution(inputArray) = 3.

Input/Output
[execution time limit] 4 seconds (py3)
[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 10,
-15 ≤ inputArray[i] ≤ 15.

[output] integer
The maximal absolute difference.
'''


def solution(inputArray):
    result = 0
    for x in range(len(inputArray)-1):
        result = max(result, abs(inputArray[x] - inputArray[x+1]))
    return result


inputArray = [2, 4, 1, 0]
assert solution(inputArray) == 3
