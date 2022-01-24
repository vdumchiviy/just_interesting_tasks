'''
Correct variable names consist only of English letters, 
digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be solution(name) = true;
For name = "qq-q", the output should be solution(name) = false;
For name = "2w2", the output should be solution(name) = false.
Input/Output

[execution time limit] 4 seconds (py3)
[input] string name
Guaranteed constraints:
1 ≤ name.length ≤ 10.
[output] boolean
true if name is a correct variable name, false otherwise.
'''
def solution(name):
    alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_0123456789"
    not_first = "0123456789"
    if name[0] in not_first:
        return False
    if len(list(filter(lambda x: x not in alphabet, name))) > 0:
        return False
    return True

assert solution("var_1__Int") is True
assert solution("qq-q") is False
assert solution("2w2") is False
# assert solution() is 
# assert solution() is 
# assert solution() is 
