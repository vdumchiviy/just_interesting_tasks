'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
the output should be

solution(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.boolean matrix

A non-empty rectangular matrix consisting of boolean values - True if the corresponding cell contains a mine, False otherwise.

Guaranteed constraints:
2 ≤ matrix.length ≤ 100,
2 ≤ matrix[0].length ≤ 100.

[output] array.array.integer

Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.
'''


def solution(matrix):
    def get_value(r, c):
        if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[r]):
            return 0
        else:
            return 1 if matrix[r][c] else 0

    result = list()
    for row in range(len(matrix)):
        element = list()
        for col in range(len(matrix[row])):
            element.append(get_value(row-1, col-1)+get_value(row-1, col)+get_value(row-1, col+1) +
                           get_value(row, col-1) + get_value(row, col+1) +
                           get_value(row+1, col-1)+get_value(row+1, col)+get_value(row+1, col+1))
        result.append(element)
    return result


matrix = [[True, False, False, True],
          [False, False, True, False],
          [True, True, False, True]]
assert solution(matrix) == [[0, 2, 2, 1],
                            [3, 4, 3, 3],
                            [1, 2, 3, 1]]
