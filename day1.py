"""https://adventofcode.com/2020/day/1"""

with open('inputs/day1.txt', 'r') as input_file:
    expense_report = sorted(map(int, input_file.readlines()))


def puzzle_1():
    while expense_report:
        current_value = expense_report.pop()
        if 2020 - current_value in expense_report:
            print(current_value * (2020 - current_value))
            break


def puzzle_2():
    while expense_report:
        current_value = expense_report.pop()
        missing = 2020 - current_value
        leftovers = list(filter(lambda x: x < missing, expense_report))
        while leftovers:
            current_leftover = leftovers.pop()
            if missing - current_leftover in leftovers:
                print(current_value * current_leftover * (missing - current_leftover))


# puzzle_1()
puzzle_2()
