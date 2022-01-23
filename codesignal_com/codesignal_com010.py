'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''


def solution(a):

    def get_next_human_position():
        for x in range(position, len(a)):
            if a[x] != -1:
                return x

    rev_a = sorted(list(filter(lambda x: x >= 0, a)))
    position = 0
    for human in range(len(rev_a)):
        position = get_next_human_position()
        a[position] = rev_a[human]
        position += 1
    return a


a = [-1, 150, 190, 170, -1, -1, 160, 180]
assert solution(a) == [-1, 150, 160, 170, -1, -1, 180, 190]

a = [-1]
assert solution(a) == [-1]
a = [-1, -1, -1, -1, -1]
assert solution(a) == [-1, -1, -1, -1, -1]
