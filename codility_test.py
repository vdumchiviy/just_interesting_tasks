'''This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.'''


def solution1(A):
    # write your code in Python 3.6
    if max(A) <= 0:
        result = 1
    else:
        sorted_A = list(sorted(set(A)))
        initial = sorted_A[0]
        counter = 0
        for x in range(len(sorted_A)):
            if sorted_A[x] != initial + counter:
                result = sorted_A[x-1] + 1
                break
            else:
                counter += 1
        if result == 0:
            result = max(A) + 1

    return result


def solution(A):
    # write your code in Python 3.6
    result = 1
    if max(A) <= 0:
        result = 1
    else:
        b = set(range(min(A), max(A)+1))
        c = set(A).symmetric_difference(b)
        if len(c) == 0:
            result = max(A) + 1
        elif len(c) == 1:
            result = c.pop()
        else:
            result = min(c)

    return result


A = [1, 3, 6, 4, 1, 2, 8]
assert solution(A) == 5
A = [1, 2, 3]
assert solution(A) == 4
A = [-1, -3]
assert solution(A) == 1
A = [-1000, 0]
assert solution(A) == 1
A = [-1, -1, -1, 0, 0, 0, 0, 2, 2, 2, 2]
assert solution(A) == 1
A = [-1000000, 1000000]
assert solution(A) == 1