"""https://adventofcode.com/2020/day/13"""
import math

with open("inputs/day13.txt", "r") as input_file:
    earliest_depart = int(input_file.readline().strip())
    bus_ids = list(
        map(
            lambda x: int(x) if x != "x" else x,
            input_file.readline().strip().split(","),
        )
    )


def puzzle_1():
    active_bus_ids = list(filter(lambda x: x != "x", bus_ids))

    waiting_till = earliest_depart
    while True:
        for bus_id in active_bus_ids:
            if waiting_till % bus_id == 0:
                return (waiting_till - earliest_depart) * bus_id
        waiting_till += 1


def puzzle_2():
    active_bus_ids_and_pos = [
        (bus, pos) for pos, bus in enumerate(bus_ids) if bus != "x"
    ]
    first_bus_id = active_bus_ids_and_pos[0][0]

    active_bus_ids_and_pos = set(active_bus_ids_and_pos)

    waiting_till = first_bus_id
    skip = set()
    while True:
        for bus, pos in active_bus_ids_and_pos.difference(skip):
            if (waiting_till + pos) % bus == 0:
                skip.add((bus, pos))
        if len(active_bus_ids_and_pos) == len(skip):
            return waiting_till
        waiting_till += math.lcm(*(bus for bus, _ in skip))


# print(puzzle_1())
print(puzzle_2())
