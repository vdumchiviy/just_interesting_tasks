'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be solution(inputArray) = 4.
0+4=4, 4+4=8, 8+4=12

Input/Output
[execution time limit] 4 seconds (py3)
[input] array.integer inputArray
Non-empty array of positive integers.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 1000,
1 ≤ inputArray[i] ≤ 1000.

[output] integer
The desired length.
'''


def solution(inputArray):
    step = 1
    # obstacles = sorted(inputArray)
    max_value = max(inputArray)
    while True:
        step += 1
        pos = 0
        while pos <= max_value:
            pos += step
            if pos in inputArray:
                break
        if pos > max_value:
            return step


assert solution([5, 3, 6, 7, 9]) == 4
assert solution([2, 3]) == 4
assert solution([1, 4, 10, 6, 2]) == 7
assert solution([1000, 999]) == 6
assert solution([5, 8, 9, 13, 14]) == 6
