import copy


def solution(A):
    # write your code in Python 3.6
    total_pollution = sum(A)
    goal = total_pollution / 2.0
    factories = list()
    factories = copy.deepcopy(A)
    filters = 0
    while sum(factories) > goal:
        max_f = max(factories)
        factories[factories.index(max_f)] = max_f / 2
        filters += 1
    print(filters)
    return filters


A = [5, 19, 8, 1]
solution(A)
A = [10, 10]
solution(A)
A = [3, 0, 5]
solution(A)
A = [33, 4, 3, 4]
solution(A)
