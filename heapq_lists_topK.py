import heapq


"""
Есть список состоящий из L сортированных списков, в каждом из которых элементы уникальны.
Например: """
lists = [
    [1, 2, 3],
    [3, 4, 8],
    [1, 8],
    [1, 5, 8, 11, 19]
]

"""
[1,1,1,1,2,3,3,4,8,8,8]
Нужно написать функцию topK, которая возвращает К самых частотных элементов в этой структуре.
Полным решением будет оптимальное с точки зрения памяти - не более O(K + L) доппамяти.
"""


class HeapSeq():
    lists = list()
    heap = list()
    list_max_len = 0
    lists_positions = list()

    def __init__(self, lists: list):
        self.lists = lists

    def __iter__(self):
        i = 0
        for l in lists:
            self.list_max_lenlist_max_len = max(self.list_max_len, len(l))
            self.lists_positions.append([1, len(l)])
            heapq.heappush(self.heap, [l[0], i])
            i += 1
        return self

    def __next__(self):

        if self.heap:
            result, list_number = heapq.heappop(self.heap)
            if self.lists_positions[list_number][0] < self.lists_positions[list_number][1]:
                heapq.heappush(
                    self.heap,
                    [self.lists[list_number][self.lists_positions[list_number][0]], list_number])
                self.lists_positions[list_number][0] += 1
        else:
            raise StopIteration
        return result


def test1_topK(lists: list, K: int) -> list:

    # heap = []

    # heapq.heappush(heap, lists[0][0])
    # heapq.heappush(heap, lists[1][0])
    # heapq.heappush(heap, lists[2][0])
    # heapq.heappush(heap, lists[0][1])
    # heapq.heappush(heap, lists[1][1])
    # heapq.heappush(heap, lists[2][1])
    # heapq.heappush(heap, lists[0][2])
    # heapq.heappush(heap, lists[1][2])

    heap = []
    print()
    len_list = len(lists)
    i = 0
    pos = 0
    list_max_len = 0
    enumerator_list = []
    lists_positions = []
    for l in lists:
        list_max_len = max(list_max_len, len(l))
        lists_positions.append([1, len(l)])
        heapq.heappush(heap, [l[0], i])
        i += 1

    while heap:
        out_value, list_number = heapq.heappop(heap)
        enumerator_list.append(out_value)
        if lists_positions[list_number][0] < lists_positions[list_number][1]:
            heapq.heappush(
                heap, [lists[list_number][lists_positions[list_number][0]], list_number])
            lists_positions[list_number][0] += 1

    # while pos < list_max_len:
    #     i = 0
    #     while i < len_list:
    #         if pos < len(lists[i]) - 1:
    #             n = lists[i][pos]
    #             heapq.heappush(heap, n)
    #         i += 1
    #     pos += 1
    # print(heapq.heapify(lists))
    return enumerator_list


def topK(lists: list, k: int) -> list:
    """This function returns K elements that appear the most times in the lists

    Args:
        lists (list): [list of lists which contains ordered numbers]
        K (int): [max count of the most common numbers]

    Returns:
        list: [list contains K elements that appear the most times in the source lists]
    """
    # heap_sequence = HeapSeq(lists)
    # s = ''
    # for x in heap_sequence:
    #     s += ' ' + str(x)
    # print(s)
    out_list = list()
    heap_sequence2 = HeapSeq(lists)
    old_value: int = None
    old_pos = -1
    pos = 0
    for value in heap_sequence2:
        if pos == 0:
            old_value = value
        if value != old_value:
            count = pos - old_pos - 1
            old_pos = pos - 1
            print(f"значение {old_value} встречается раз: {count}")
            out_list.append([count, old_value])
            old_value = value

        print(value)
        pos += 1
    count = pos - old_pos - 1
    print(f"значение {old_value} встречается раз: {count}")
    out_list.append([count, value])

    # here I can try change list to heap with an item's structure [count, value]
    # but now i use a simple structure for a demonstration of an algorhytm
    out_list.sort(reverse=True)
    print(out_list)
    result = []
    for x in range(k):
        result.append(out_list[x][1])

    return result


print(topK(lists, 3))


# print(test1_topK(lists, 3))
