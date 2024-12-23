"""
--- Day 3: Mull It Over ---
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

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

