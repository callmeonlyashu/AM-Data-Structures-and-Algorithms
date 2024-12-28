"""
--- Day 2: Red-Nosed Reports ---
https://adventofcode.com/2024/day/2
"""

arr = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]


def extract_data_from_file():
    with open("input_day_2.txt") as f:
        content = f.read()

    rows = content.split("\n")

    data = []
    for r in rows:
        row_data = [int(value) for value in r.split(" ")]
        data.append(row_data)
    return data


def check_current_diff_report(arr):
    sorted_order = all(num > 0 for num in arr) or all(num < 0 for num in arr)

    if sorted_order:
        actual_report = all(i in [-1, -2, -3, 1, 2, 3] for i in arr)
    else:
        actual_report = False
    return actual_report


def get_current_diff(row):
    curr_diff = []
    for i in range(len(row)):
        if i + 1 < len(row):
            curr_diff.append(row[i + 1] - row[i])

    return curr_diff


def safe_reports_count(arr=None):
    if arr:
        data = arr
    else:
        data = extract_data_from_file()

    safe_count = 0
    for row in data:
        curr_diff = get_current_diff(row)
        if check_current_diff_report(curr_diff):
            safe_count += 1
        else:
            for p in range(len(row)):
                arr_removed_element = row[:p] + row[p + 1:]
                curr_diff = get_current_diff(arr_removed_element)
                if check_current_diff_report(curr_diff):
                    safe_count += 1
                    break

    return safe_count


a = safe_reports_count()
1==1
