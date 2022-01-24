'''
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be solution(n) = true;
For n = 642386, the output should be solution(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 109.

[output] boolean

true if all digits of n are even, false otherwise.
'''
def solution(n):
    for x in str(n):
        if int(x) % 2 != 0:
            return False
    return True

n = 248622
assert solution(n) is True

n = 642386
assert solution(n) is False