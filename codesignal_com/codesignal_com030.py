'''
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements
 in such a way that each consecutive pair of strings differ by exactly one character.
  Return true if it's possible, and false if not.
Note: You're only rearranging the order of the strings, not the order of the letters within the strings!
355 / 5 000
Результаты перевода
Учитывая массив строк одинаковой длины, вы хотели бы знать, возможно ли изменить порядок элементов
  таким образом, чтобы каждая последовательная пара строк отличалась ровно на один символ.
   Верните true, если это возможно, и false, если нет.
Примечание. Вы меняете только порядок строк, а не порядок букв в строках! 
Example

For inputArray = ["aba", "bbb", "bab"], the output should be solution(inputArray) = false.
There are 6 possible arrangements for these strings:
["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be solution(inputArray) = true.
It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character
 (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

Input/Output    
[execution time limit] 4 seconds (py3)
[input] array.string inputArray
A non-empty array of strings of lowercase letters.
Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 15.

[output] boolean

Return true if the strings can be reordered in such a way that each neighbouring pair of strings differ by exactly one character (false otherwise).
'''
import itertools


def solution(inputArray):
    def check_perms(perm):
        count = 0
        for x in range(len(perm)-1):
            if perm[x] == perm[x+1]:
                return False
            if len(list(filter(lambda x: x[0] != x[1], zip(perm[x], perm[x+1])))) > 1:
                return False
        return True

    perm_set = itertools.permutations(inputArray)
    for perm in perm_set:
        if check_perms(perm):
            return True
    return False


assert solution(["aba", "bbb", "bab"]) is False
assert solution(["ab", "bb", "aa"]) is True
assert solution(["zzzzab",
                 "zzzzbb",
                 "zzzzaa"]) is True
assert solution(["q", "q"]) is False
assert solution(["ab",
                 "ad",
                 "ef",
                 "eg"]) is False
print(solution.MRO)