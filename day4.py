"""https://adventofcode.com/2020/day/4"""
import re
from curses.ascii import isdigit

with open('inputs/day4.txt', 'r') as input_file:
    blank_line_regex = r"(?:\r?\n){2,}"
    passports = re.split(blank_line_regex, input_file.read().strip())
    passports = [p.replace('\n', ' ') for p in passports]


def puzzle_1():
    required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    valid = 0
    for p in passports:
        if all(r in p for r in required):
            valid += 1
    return valid


def puzzle_2():

    def four_digits(x):
        return len(x) == 4 and x.isnumeric()

    fields = {
        'byr': lambda x: four_digits(x) and (1920 <= int(x) <= 2002),
        'iyr': lambda x: four_digits(x) and (2010 <= int(x) <= 2020),
        'eyr': lambda x: four_digits(x) and (2020 <= int(x) <= 2030),
        'hgt': lambda x: (
            (x.endswith('cm') and (150 <= int(x.strip('cm')) <= 193)) or
            (x.endswith('in') and (59 <= int(x.strip('in')) <= 76))
        ),
        'hcl': lambda x: (
            x.startswith('#') and
            len(x.strip('#')) == 6 and
            len(re.findall(r'[a-f0-9]', x[1:])) == 6
        ),
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: x.isnumeric() and len(x) == 9,
        'cid': lambda x: True
    }
    fields_keys = fields.keys()

    valid = 0
    for p in passports:
        if not all(r in p for r in fields_keys if r != 'cid'):
            continue

        fields_and_values = list(x.split(':') for x in p.split())

        if all(fields[field](value) for field, value in fields_and_values):
            valid += 1

    return valid


# print(puzzle_1())
print(puzzle_2())
