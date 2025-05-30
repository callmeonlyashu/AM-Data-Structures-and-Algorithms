"""
https://adventofcode.com/2024/day/3
"""


def extract_data_from_file():
    with open("input_day_3.txt") as f:
        content = f.read()

    return content


def mul(x,y):
    return x*y


def mull_it_over(param=None):
    if param:
        data = param
    else:
        data = extract_data_from_file()

    split_mul = data.split("mul(")
    round_2_splits = []
    for i in split_mul:
        if ")" in i:
            round_2_splits.extend(i.split(")"))

    multiply_str = []
    for j in round_2_splits:
        multiply_str.append(f"mul({j})")

    result = 0
    for actual_str in multiply_str:
        try:
            result += eval(actual_str)
        except:
            pass


def mull_it_over_part_2(param=None):
    if param:
        data = param
    else:
        data = extract_data_from_file()

    data_dos = data.split("do()")

    data_do_2 = []
    for d in data_dos:
        dont_split = d.split("don't()")
        data_do_2.append(dont_split[0])

    final_operatable_data = "".join(data_do_2)
    split_mul = final_operatable_data.split("mul(")
    round_2_splits = []
    for i in split_mul:
        if ")" in i:
            round_2_splits.extend(i.split(")"))

    multiply_str = []
    for j in round_2_splits:
        multiply_str.append(f"mul({j})")

    result = 0
    for actual_str in multiply_str:
        try:
            result += eval(actual_str)
        except:
            pass


if __name__ == '__main__':
    # sum1 = mull_it_over("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    # sum2 = mull_it_over()

    # sum1 = mull_it_over_part_2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    sum2 = mull_it_over_part_2()

