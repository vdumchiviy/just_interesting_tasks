'''After becoming famous, the CodeBots decided to move into a new building together. 
Each of the rooms has a different cost, and some of them are free, but there's a rumour 
that all the free rooms are haunted! Since the CodeBots are quite superstitious, 
they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents 
the cost of the room, your task is to return the total sum of all rooms that are suitable 
for the CodeBots (ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
solution(matrix) = 9.'''


def solution(matrix):
    # template = [0 if x == 0 else 1 for x in matrix[0]]
    template = [1 for x in matrix[0]]
    result = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                if template[x] != 0:
                    template[x] = 0
            else:
                if template[x] != 0:
                    result += matrix[y][x]
    return result


matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
assert solution(matrix) == 9
matrix = [[1, 0, 10, 1, 6, 5, 4, 0],
          [6, 2, 0, 1, 2, 4, 5, 10],
          [0, 1, 2, 6, 8, 9, 6, 0]
          ]
assert solution(matrix) == 74
