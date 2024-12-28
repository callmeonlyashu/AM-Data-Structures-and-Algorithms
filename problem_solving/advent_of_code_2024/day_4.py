import copy


def extract_data_from_file():
    with open("input_day_4.txt") as f:
        content = f.read()
    return content


def create_2d_array(str_params):
    rows = str_params.strip().split("\n")  # Added strip to remove trailing newline
    result = []
    for r in rows:
        result.append(list(r))
    return result


def get_row_wise_count(arr):
    count = 0
    for row in arr:
        for i in range(len(row) - 3):  # Fixed index boundary check to prevent out-of-range error
            string_arr = row[i:i+4]
            string = "".join(string_arr)
            if string in ['XMAS', 'SAMX']:
                count += 1
    return count


def get_column_wise_count(arr):
    transpose_column = copy.deepcopy(arr)
    for i in range(len(arr)):  # Fixed loop to correctly iterate over rows
        for j in range(len(arr[0])):  # Fixed loop to iterate over columns
            transpose_column[i][j] = arr[j][i]

    count = get_row_wise_count(transpose_column)

    return count


def get_diagonal_wise_count(arr):
    res = []
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            i = row
            j = col
            num = []
            while i < len(arr) and j < len(arr[0]):  # Added boundary checks
                num.append(arr[i][j])
                i += 1
                j += 1
                if len(num) == 4:
                    res.append(num)
                    break  # Break once we collect a 4-character diagonal

    res_filtered = [x for x in res if len(x) == 4]
    res_string = [''.join(x) for x in res_filtered]

    res_reverse = []
    for row in range(len(arr)):
        for col in range(len(arr[row]) - 1, -1, -1):  # Fixed range to include column 0
            i = row
            j = col
            num = []
            while i < len(arr) and j >= 0:  # Added boundary checks
                num.append(arr[i][j])
                i += 1
                j -= 1
                if len(num) == 4:
                    res_reverse.append(num)
                    break  # Break once we collect a 4-character reverse diagonal

    res_rev_filtered = [x for x in res_reverse if len(x) == 4]
    res_rev_string = [''.join(x) for x in res_rev_filtered]

    final_array = res_rev_string + res_string

    result_count = 0
    for st in final_array:
        if st in ["XMAS", "SAMX"]:
            result_count += 1
    return result_count


def extract_xmas(param=None):
    if param:
        data = param
    else:
        data = extract_data_from_file()

    arr = create_2d_array(data)
    row_wise_count = get_row_wise_count(arr)
    column_wise_count = get_column_wise_count(arr)
    diagonal_wise_count = get_diagonal_wise_count(arr)
    total_count = row_wise_count + column_wise_count + diagonal_wise_count
    print(f"Total count: {total_count}")
    return total_count


def extract_xmas_part_2(param=None):
    if param:
        data = param
    else:
        data = extract_data_from_file()

    arr = create_2d_array(data)

    result_count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            num = []
            count = 0
            m = i
            n = j
            while m < len(arr):
                while n < len(arr[0]):
                    if count < 3:
                        num.append(arr[m][n])
                        count += 1
                    break
                m += 1
                n += 1

            joined_string = ''.join(num)
            if joined_string in ['MAS', 'SAM']:
                l = j + 2
                k = i
                count_2 = 0
                num_2 = []
                while k < len(arr):
                    while l >= 0 and l < len(arr[0]):
                        if count_2 < 3:
                            num_2.append(arr[k][l])
                            count_2 += 1
                        break
                    k += 1
                    l -= 1
                joined_string_2 = ''.join(num_2)
                if joined_string_2 in ['MAS', 'SAM']:
                    result_count += 1
    return result_count


if __name__ == '__main__':
    param = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    # extract_xmas()

    extract_xmas_part_2()