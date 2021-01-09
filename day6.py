"""https://adventofcode.com/2020/day/6"""
import re


with open("inputs/day6.txt", "r") as input_file:
    blank_line_regex = r"(?:\r?\n){2,}"
    groups = re.split(blank_line_regex, input_file.read().strip())
    groups = [g.replace("\n", " ") for g in groups]


def puzzle_1():
    return sum(len(set(x.replace(" ", ""))) for x in groups)


def puzzle_2():
    counter = 0
    for group in groups:
        counter += len(set.intersection(*(set(x) for x in group.split())))
    return counter


# print(puzzle_1())
print(puzzle_2())
