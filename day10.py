"""https://adventofcode.com/2020/day/10"""
from collections import defaultdict
from functools import lru_cache

with open("inputs/day10.txt", "r") as input_file:
    numbers = list(map(int, input_file.readlines()))

numbers.append(0)
numbers = sorted(numbers)


def puzzle_1():
    diff_1 = 0
    diff_3 = 0
    for i in range(len(numbers) - 1):
        if numbers[i] + 1 == numbers[i + 1]:
            diff_1 += 1
        if numbers[i] + 3 == numbers[i + 1]:
            diff_3 += 1
    diff_3 += 1
    return diff_1 * diff_3


def puzzle_2():
    n = numbers
    n_max = max(n) + 3
    n.append(n_max)
    max_index = len(n) - 1

    edges = []
    for i in range(max_index):
        if n[i + 1] - n[i] <= 3:
            edges.append((n[i], n[i + 1]))
        if i + 2 <= max_index and n[i + 2] - n[i] <= 3:
            edges.append((n[i], n[i + 2]))
        if i + 3 <= max_index and n[i + 3] - n[i] == 3:
            edges.append((n[i], n[i + 3]))

    edges_dict = defaultdict(list)
    for e in edges:
        edges_dict[e[0]].append(e)

    @lru_cache()
    def path_finder(edge):
        if edge[1] == n_max:
            return 1
        return sum(path_finder(e) for e in edges_dict[edge[1]])

    return sum(path_finder(e) for e in edges_dict[0])


# print(puzzle_1())
print(puzzle_2())
