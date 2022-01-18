def solution(P, S):
    # write your code in Python 3.6
    S_sorted = sorted(S, reverse=True)
    friends = sum(P)
    seats = 0
    cars = 0
    for x in S_sorted:
        cars += 1
        seats += x
        if seats >= friends:
            break
    print(cars)
    return cars

P = [2, 3, 4, 2]
S = [2, 5, 7, 2]
# solution(P, S)
# assert solution(P, S) == 2

P = [1,2,1]
S = [1,1,2]
assert solution(P, S) == 3

P = [4,4,2,4]
S = [5,5,2,5]
# solution(P, S)

P = [4,4,3,4]
S = [4,4,3,4]
# solution(P, S)

P = [4]
S = [5]
# solution(P, S)