"""https://adventofcode.com/2020/day/11"""
from copy import deepcopy

with open('inputs/day11.txt', 'r') as input_file:
    seats = list(map(lambda x: list(x.replace('\n', '')), input_file.readlines()))


def print_seats(s):
    for row in s:
        print(''.join(row))
    print()


def puzzle_1():
    height = len(seats)
    width = len(seats[0])

    def processed_seat(r, c, _old_seats, _new_seats):
        seat = _old_seats[r][c]
        if seat == '.':
            return False

        seats_around = []
        for s_c, s_r in (
            (c - 1, r - 1), (c, r - 1), (c + 1, r - 1),
            (c - 1, r),                 (c + 1, r),
            (c - 1, r + 1), (c, r + 1), (c + 1, r + 1),
        ):
            try:
                if s_c >= 0 and s_r >= 0:
                    seats_around.append(_old_seats[s_r][s_c])
            except IndexError:
                pass
        occupied_around = len(list(filter(lambda i: i == '#', seats_around)))
        if seat == 'L' and occupied_around == 0:
            _new_seats[r][c] = '#'
            return True
        if seat == '#' and occupied_around >= 4:
            _new_seats[r][c] = 'L'
            return True
        return False

    old_seats = deepcopy(seats)
    while 1:
        has_changed = False
        new_seats = deepcopy(old_seats)
        for row_id in range(height):
            for column_id in range(width):
                has_changed = processed_seat(row_id, column_id, old_seats, new_seats) or has_changed
        if not has_changed:
            break
        old_seats = deepcopy(new_seats)

    return ''.join(''.join(x) for x in old_seats).count('#')


def puzzle_2():
    height = len(seats)
    width = len(seats[0])

    def processed_seat(r, c, _old_seats, _new_seats):
        seat = _old_seats[r][c]
        if seat == '.':
            return False

        seats_around = []
        for direction_c, direction_r in (
                (-1, -1), (0, -1), (1, -1),
                (-1, 0),           (1, 0),
                (-1, 1),  (0, 1),  (1, 1),
        ):
            s_c, s_r = c + direction_c, r + direction_r
            while 0 <= s_c < width and 0 <= s_r < height:
                s = _old_seats[s_r][s_c]
                if s != '.':
                    seats_around.append(_old_seats[s_r][s_c])
                    break
                s_c += direction_c
                s_r += direction_r

        occupied_around = len(list(filter(lambda i: i == '#', seats_around)))
        if seat == 'L' and occupied_around == 0:
            _new_seats[r][c] = '#'
            return True
        if seat == '#' and occupied_around >= 5:
            _new_seats[r][c] = 'L'
            return True
        return False

    old_seats = deepcopy(seats)
    while 1:
        has_changed = False
        new_seats = deepcopy(old_seats)
        for row_id in range(height):
            for column_id in range(width):
                has_changed = processed_seat(row_id, column_id, old_seats, new_seats) or has_changed
        if not has_changed:
            break
        old_seats = deepcopy(new_seats)

    return ''.join(''.join(x) for x in old_seats).count('#')


# print(puzzle_1())
print(puzzle_2())
