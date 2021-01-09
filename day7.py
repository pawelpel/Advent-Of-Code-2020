"""https://adventofcode.com/2020/day/7"""
import re

with open("inputs/day7.txt", "r") as input_file:
    raw_rules = input_file.readlines()


def from_text(raw_rule):
    raw_rule = raw_rule.replace("\n", "")
    match = re.match(r"(.*?) bags contain (.*).", raw_rule)

    name = match.group(1)

    children = re.findall(r"((\d) (\w+? \w+?) bag[s]?[,\.]?)", match.group(2))
    children = list(map(lambda x: (x[1], x[2]), children))

    return name, children


def puzzle_1():
    rules = {}
    rule_names_with_gold = set()

    for raw_rule in raw_rules:
        name, children = from_text(raw_rule)
        rules[name] = children
        if any(x[1] == "shiny gold" for x in children):
            rule_names_with_gold.add(name)

    colors = set(rule_names_with_gold)

    def search_for_outermost_bags(name):
        next_names = set()
        for n, c in rules.items():
            child_names = set(map(lambda x: x[1], c))
            if name in child_names:
                next_names.add(n)
                colors.add(n)

        for n in next_names:
            search_for_outermost_bags(n)

    for name in rule_names_with_gold:
        search_for_outermost_bags(name)

    return len(colors)


def puzzle_2():
    rules = {}

    for raw_rule in raw_rules:
        name, children = from_text(raw_rule)
        rules[name] = children

    def recursive_bag_counter(bag_name):
        bags_inside = rules[bag_name]

        counter = 0
        for n_b, b in bags_inside:
            n_b = int(n_b)
            counter += n_b
            counter += n_b * recursive_bag_counter(b)
        return counter

    return recursive_bag_counter("shiny gold")


# print(puzzle_1())
print(puzzle_2())
