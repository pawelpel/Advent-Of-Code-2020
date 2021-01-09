"""https://adventofcode.com/2020/day/14"""
import re

with open("inputs/day14.txt", "r") as input_file:
    program = [x.replace("\n", "") for x in input_file.readlines()]


def apply_mask(mask, binary_string):
    binary_string = binary_string.rjust(36, "0")
    return "".join([v if m == "X" else m for v, m in zip(binary_string, mask)])


def puzzle_1():
    mem = {}

    mem_pattern = re.compile(r"mem\[(\d+)] = (\d+)")

    current_mask = ""
    for line in program:
        if line.startswith("mask"):
            current_mask = line.split("=")[1].strip()
        else:
            match = re.match(mem_pattern, line)
            address = int(match.group(1))
            value = int(match.group(2))

            binary_string = str(bin(value))[2:]

            mem[address] = int(apply_mask(current_mask, binary_string), 2)

    return sum(mem.values())


def puzzle_2():
    return


# print(puzzle_1())
print(puzzle_2())
