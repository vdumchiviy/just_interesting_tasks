# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(message, K):
    # write your code in Python 3.6
    result = ''
    if len(message) <= K:
        result = message
    elif message[K] == " ":
        result = message[0:K] 
    else:
        for x in range(K-1, 0, -1):
            if message[x] == " ":
                result = message[0:x]
                break
    return result

message = "The quick brown fox jumps over the lazy dog"
K = 43
assert solution(message, K) == "The quick brown fox jumps over the lazy dog"

message = "The quick brown fox jumps over the lazy dog"
K = 39
assert solution(message, K) == "The quick brown fox jumps over the lazy"

message = 'Codility, we test coders'
K = 14
assert solution(message, K) == 'Codility, we'

message = "To crop ornot to crop"
K = 21
assert solution(message, K) == "To crop ornot to crop"

message = "One"
K = 15
assert solution(message, K) == "One"

message = "O n"
K = 1
assert solution(message, K) == "O"

message = "O n"
K = 2
assert solution(message, K) == "O"

message = "O n"
K = 3
assert solution(message, K) == "O n"
