'''
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be solution(cell1, cell2) = true.
For cell1 = "A1" and cell2 = "H3", the output should be solution(cell1, cell2) = false.

Input/Output
[execution time limit] 4 seconds (py3)
[input] string cell1
Guaranteed constraints:
cell1.length = 2,
'A' ≤ cell1[0] ≤ 'H',
1 ≤ cell1[1] ≤ 8.

[input] string cell2
Guaranteed constraints:
cell2.length = 2,
'A' ≤ cell2[0] ≤ 'H',
1 ≤ cell2[1] ≤ 8.

[output] boolean
true if both cells have the same color, false otherwise.
'''


def solution(cell1, cell2):
    letters = "ABCDEFGH"
    digits = "12345678"
    if (letters.find(cell1[0]) % 2 == letters.find(cell2[0]) % 2
        and digits.find(cell1[1]) % 2 == digits.find(cell2[1]) % 2) or \
        (letters.find(cell1[0]) % 2 != letters.find(cell2[0]) % 2
         and digits.find(cell1[1]) % 2 != digits.find(cell2[1]) % 2):
        return True
    else:
        return False


assert solution("A1", "C3") is True
assert solution("A1", "H3") is False
