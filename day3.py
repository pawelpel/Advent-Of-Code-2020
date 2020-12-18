"""https://adventofcode.com/2020/day/3"""
from dataclasses import dataclass
from functools import reduce
from operator import mul

with open('inputs/day3.txt', 'r') as input_file:
    given_map = [list(x.replace('\n', '')) for x in input_file.readlines()]


def puzzle_1(right=None, down=None):
    if not right or not down:
        right, down = 3, 1

    height, width = len(given_map), len(given_map[0])

    @dataclass
    class Position:
        x: int = 0
        y: int = 0

    current_pos = Position()

    trees = 0

    while current_pos.y < height - 1:

        if current_pos.x + right > width - 1:
            current_pos.x = (right - 1) - (width - 1 - current_pos.x)
        else:
            current_pos.x += right

        current_pos.y += down

        if given_map[current_pos.y][current_pos.x] == "#":
            trees += 1

    return trees


def puzzle_2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    return reduce(mul, (puzzle_1(*x) for x in slopes))


# print(puzzle_1())
print(puzzle_2())
