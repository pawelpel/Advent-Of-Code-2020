"""https://adventofcode.com/2020/day/5"""

with open('inputs/day5.txt', 'r') as input_file:
    boarding_passes = [x.replace('\n', '') for x in input_file.readlines()]


def puzzle_1():
    max_seat_id = 0

    def get_half(x: list, half_sign):
        l = int(len(x)/2)
        if half_sign in ('F', 'L'):
            return x[:l]
        return x[l:]

    for boarding_pass in boarding_passes:

        rows = list(range(128))
        for i in boarding_pass[:7]:
            rows = get_half(rows, i)
        given_row = rows[0]

        columns = list(range(8))
        for i in boarding_pass[7:]:
            columns = get_half(columns, i)
        given_column = columns[0]

        seat_id = given_row * 8 + given_column
        max_seat_id = max(seat_id, max_seat_id)

    return max_seat_id


def puzzle_2():

    def get_half(x: list, half_sign):
        l = int(len(x)/2)
        if half_sign in ('F', 'L'):
            return x[:l]
        return x[l:]

    seats = []

    for boarding_pass in boarding_passes:

        rows = list(range(128))
        for i in boarding_pass[:7]:
            rows = get_half(rows, i)
        given_row = rows[0]

        columns = list(range(8))
        for i in boarding_pass[7:]:
            columns = get_half(columns, i)
        given_column = columns[0]

        seat_id = given_row * 8 + given_column
        seats.append(seat_id)

    seats = sorted(seats)
    for i in range(seats[0], seats.pop()):
        if i not in seats:
            return i

# print(puzzle_1())
print(puzzle_2())
