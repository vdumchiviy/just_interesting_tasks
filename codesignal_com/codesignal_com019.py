'''An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example
For inputString = "172.16.254.1", solution(inputString) = true;
For inputString = "172.316.254.1", solution(inputString) = false. 316 is not in range [0, 255].
For inputString = ".254.255.0", solution(inputString) = false. There is no first number.

IPv4 address
An identification number for devices connected to the internet. An IPv4 addresses written in dotted quad notation
consists of four 8-bit integers separated by periods.

In other words, it's a string of four numbers each between 0 and 255 inclusive, with a "." character in between each number.
All numbers should be present without leading zeros.

Examples:

192.168.0.1 is a valid IPv4 address
255.255.255.255 is a valid IPv4 address
280.100.92.101 is not a valid IPv4 address because 280 is too large to be an 8-bit integer (the largest 8-bit integer is 255)
255.100.81.160.172 is not a valid IPv4 address because it contains 5 integers instead of 4
1..0.1 is not a valid IPv4 address because it's not properly formatted
17.233.00.131 and 17.233.01.131 are not valid IPv4 addresses because they contain leading zeros

[execution time limit] 4 seconds (py3)
[input] string inputString
A string consisting of digits, full stops and lowercase English letters.
Guaranteed constraints:
1 ≤ inputString.length ≤ 30.
[output] boolean
true if inputString satisfies the IPv4 address naming rules, false otherwise.
'''


def solution(inputString: str):

    def get_next_digit(start, level):
        def is_dig_OK(digit):
            if digit == "0":
                return True
            if not digit.isdigit() or len(digit) == 0 or digit[0] == "0" or int(digit) < 0 or int(digit) > 255:
                return False

            return True
        level += 1
        if level == 5:
            if start == -1:
                return True
            else:
                return False
        else:
            if start == -1:
                return False

        # start += 1
        if start == -1:
            return get_next_digit(start, level)

        pos = inputString.find(".", start)
        if pos == -1:
            digit = inputString[start:]
        else:
            digit = inputString[start:pos]
        if not is_dig_OK(digit):
            return False
        else:
            return get_next_digit((-1 if pos == -1 else pos+1), level)
    return get_next_digit(0, 0)


def solution_old(inputString: str):
    def is_dig_OK(digit):
        if digit == "0":
            return True
        if not digit.isdigit() or len(digit) == 0 or digit[0] == "0" or int(digit) < 0 or int(digit) > 255:
            return False

        return True

    def get_next_digit(start):
        start += 1
        pos = inputString.find(".", start)
        if pos == -1:
            return inputString[start:], pos
        else:
            return inputString[start:pos], pos

    pos = -1
    digit, pos = get_next_digit(pos)
    if pos != -1 and is_dig_OK(digit):
        digit, pos = get_next_digit(pos)
        if pos != -1 and is_dig_OK(digit):
            digit, pos = get_next_digit(pos)
            if pos != -1 and is_dig_OK(digit):
                digit, pos = get_next_digit(pos)
                if is_dig_OK(digit):
                    if pos == -1:
                        return True
    return False


assert solution("172.16.254.1") is True
assert solution("255.255.255.255") is True
assert solution("192.168.0.1") is True
assert solution("280.100.92.101") is False
assert solution("1..0.1") is False
assert solution("17.233.00.131") is False
assert solution("255.100.81.160.172") is False
assert solution(".254.255.0") is False
assert solution("1") is False
