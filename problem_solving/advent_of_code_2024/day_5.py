"""
Link: https://adventofcode.com/2024/day/5
"""
import copy

import math


def extract_data_from_file():
    with open("input_day_5.txt") as f:
        content = f.read()

    return content


def check_page_ordering(param=None):
    if param:
        data = param
    else:
        data = extract_data_from_file()

    first_set_split = data.split("\n\n")
    rules, pages_set = first_set_split[0], first_set_split[1]

    rules = rules.split("\n")
    pages_set = pages_set.split("\n")

    pages = [p.split(",") for p in pages_set]

    correct_order_pages = []
    incorrect_order_pages = []
    for page in pages:
        to_reverse_rules = []
        for i in range(len(page)-1, -1, -1):
            for j in range(len(page)-1, -1, -1):
                if i != j and i > j:
                    to_reverse_rules.append(f"{page[i]}|{page[j]}")

        is_correct_order = True
        for rev in to_reverse_rules:
            if rev in rules:
                is_correct_order = False
                break

        if is_correct_order:
            correct_order_pages.append(page)
        else:
            incorrect_order_pages.append(page)

    result = 0
    for order_p in correct_order_pages:
        middle_index = math.floor(len(order_p)/2)
        result += int(order_p[middle_index])

    return result, incorrect_order_pages


def check_page_ordering_part_2(param=None):
    if param:
        data = param
    else:
        data = extract_data_from_file()

    first_set_split = data.split("\n\n")
    rules = first_set_split[0]

    rules = rules.split("\n")
    _, pages = check_page_ordering(param)

    # rules_set = [[int(rule.split("|")[0]), int(rule.split("|")[1])] for rule in rules]

    for pg in pages:
        for i in range(len(pg)):
            for j in range(len(pg)):
                if i != j:
                    rl = f"{pg[i]}|{pg[j]}"
                    if rl in rules:
                        pass
                    else:
                        rl_rev = f"{pg[j]}|{pg[i]}"
                        if rl_rev in rules and pg.index(pg[j]) > pg.index(pg[i]):
                            pg[i], pg[j] = pg[j], pg[i]

    result = 0
    for order_p in pages:
        middle_index = math.floor(len(order_p)/2)
        result += int(order_p[middle_index])

    return result


if __name__ == '__main__':
    param = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    # res = check_page_ordering()

    res2 = check_page_ordering_part_2()

1==1