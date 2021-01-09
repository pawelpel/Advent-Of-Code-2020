"""https://adventofcode.com/2020/day/12"""
from copy import deepcopy

with open("inputs/day12.txt", "r") as input_file:
    moves = [x.strip() for x in input_file.readlines()]


def do_a_turn(m, v, now_facing, swap_rotations=False):
    if swap_rotations:
        m = "L" if m == "R" else "R"

    d = "WNES" if m == "R" else "WSEN"
    v = v // 90
    current_direction_idx = d.index(now_facing)
    new_direction_idx = current_direction_idx + v
    if new_direction_idx > len(d) - 1:
        return d[new_direction_idx % len(d)]
    return d[new_direction_idx]


def puzzle_1():
    facing_direction = "E"
    directions = dict(N=0, S=0, E=0, W=0)

    for move in moves:
        m, value = move[0], int(move[1:])
        if m == "F":
            directions[facing_direction] += value
        elif m in ("R", "L"):
            facing_direction = do_a_turn(m, value, facing_direction)
        else:
            directions[m] += value

    return abs(directions["N"] - directions["S"]) + abs(
        directions["E"] - directions["W"]
    )


def puzzle_2():
    ship_directions = dict(N=0, S=0, E=0, W=0)
    waypoint_directions = dict(N=1, S=0, E=10, W=0)

    def recalculate(x, y, directions):
        z = directions[x] - directions[y]
        if z == 0:
            directions[x] = directions[y] = 0
        else:
            directions[x if z > 0 else y] = abs(z)
            directions[x if z < 0 else y] = 0

    for move in moves:
        m, value = move[0], int(move[1:])
        if m == "F":
            for d in ship_directions.keys():
                ship_directions[d] += value * waypoint_directions[d]
        elif m in ("R", "L"):
            rotated_directions = {}
            for d in waypoint_directions.keys():
                rotated_directions[d] = waypoint_directions[
                    do_a_turn(m, value, d, True)
                ]
            waypoint_directions = deepcopy(rotated_directions)
        else:
            waypoint_directions[m] += value
            recalculate("N", "S", waypoint_directions)
            recalculate("E", "W", waypoint_directions)

    return abs(ship_directions["N"] - ship_directions["S"]) + abs(
        ship_directions["E"] - ship_directions["W"]
    )


# print(puzzle_1())
print(puzzle_2())
