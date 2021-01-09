"""https://adventofcode.com/2020/day/9"""
from itertools import combinations

with open("inputs/day9.txt", "r") as input_file:
    numbers = list(map(int, input_file.readlines()))


def sums_up(arr, given_sum):
    return any(x + y == given_sum for x, y in combinations(arr, 2))


def puzzle_1():
    preamble = 25
    for i in range(preamble, len(numbers)):
        current_number = numbers[i]
        previous_numbers = sorted(numbers[i - preamble : i])
        if not sums_up(previous_numbers, current_number):
            return current_number


def puzzle_2():
    invalid_number = puzzle_1()

    head, tail = 0, 1
    while 1:
        s = sum(numbers[head:tail])
        if s == invalid_number:
            break
        if s < invalid_number:
            tail += 1
        if s > invalid_number:
            head += 1

    numbs = numbers[head:tail]
    return max(numbs) + min(numbs)


# print(puzzle_1())
print(puzzle_2())
