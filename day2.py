"""https://adventofcode.com/2020/day/2"""

with open("inputs/day2.txt", "r") as input_file:
    password_descriptions = [p.split() for p in input_file.readlines()]


def puzzle_1():
    count = 0
    for password_description in password_descriptions:
        policy_min, policy_max = tuple(map(int, password_description[0].split("-")))
        letter = password_description[1].replace(":", "")
        password = password_description[2]

        if policy_min <= password.count(letter) <= policy_max:
            count += 1

    print(count)


def puzzle_2():
    count = 0
    for password_description in password_descriptions:
        first_pos, second_pos = tuple(map(int, password_description[0].split("-")))
        letter = password_description[1].replace(":", "")
        password = password_description[2]

        checks = [password[x - 1] == letter for x in (first_pos, second_pos)]

        if any(checks) and not all(checks):
            count += 1

    print(count)


# puzzle_1()
puzzle_2()
