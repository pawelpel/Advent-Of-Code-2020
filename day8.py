"""https://adventofcode.com/2020/day/8"""

with open('inputs/day8.txt', 'r') as input_file:
    raw_instructions = input_file.readlines()


class SubscriptableCyclingList(list):

    def __getitem__(self, item):
        if item > len(self) - 1:
            item = item % len(self)
        return super().__getitem__(item)


instructions = SubscriptableCyclingList()
for raw_ins in raw_instructions:
    ins_name, arg = raw_ins.replace('\n', '').split()
    arg = int(arg)
    instructions.append((ins_name, arg))


def puzzle_1():
    accumulator = 0

    def acc(arg, idx):
        nonlocal accumulator
        accumulator += arg
        return idx + 1
    
    def jumps(arg, idx):
        return idx + arg
    
    def nop(_, idx):
        return idx + 1
    
    mapping = {
        'acc': acc,
        'jmp': jumps,
        'nop': nop,
    }
    
    visited_set = set()
    visited_list = list()
    
    index = 0
    while len(visited_set) == len(visited_list):
        visited_list.append(index)
        visited_set.add(index)

        instruction, argument = instructions[index]
        index = mapping[instruction](argument, index)

    return accumulator


def puzzle_2():

    def acc(arg, idx):
        nonlocal accumulator
        accumulator += arg
        return idx + 1

    def jumps(arg, idx):
        return idx + arg

    def nop(_, idx):
        return idx + 1

    mapping = {
        'acc': acc,
        'jmp': jumps,
        'nop': nop,
    }

    jmp_or_nop_instruction_indexes = [
        i for i, x in enumerate(instructions) if x[0] != 'acc'
    ]

    for to_flip in jmp_or_nop_instruction_indexes:
        accumulator = 0

        visited_set = set()
        visited_list = list()

        index = 0
        while len(visited_set) == len(visited_list):
            visited_list.append(index)
            visited_set.add(index)

            instruction, argument = instructions[index]

            if index == to_flip:
                instruction = 'jmp' if instruction == 'nop' else 'nop'

            index = mapping[instruction](argument, index)

            if index == len(instructions):
                return accumulator


# print(puzzle_1())
print(puzzle_2())
