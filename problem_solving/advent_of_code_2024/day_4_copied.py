import copy


def extract_data_from_file():
    with open("input_day_4.txt") as f:
        content = f.read()
    return content


def create_2d_array(str_params):
    rows = str_params.strip().split("\n")
    return [list(row) for row in rows]


def get_row_wise_count(arr, words, word_length):
    count = 0
    for row in arr:
        for i in range(len(row) - word_length + 1):
            string = "".join(row[i:i + word_length])
            if string in words:
                count += 1
    return count


def get_column_wise_count(arr, words, word_length):
    # Transpose using zip
    transposed = list(zip(*arr))
    return get_row_wise_count(transposed, words, word_length)


def get_diagonal_wise_count(arr, words, word_length):
    diagonals = []
    reverse_diagonals = []

    # Collect diagonals from top-left to bottom-right
    for d in range(-len(arr) + 1, len(arr[0])):
        diagonals.append([arr[i][i - d] for i in range(len(arr)) if 0 <= i - d < len(arr[0])])

    # Collect diagonals from top-right to bottom-left
    for d in range(len(arr[0]) + len(arr) - 1):
        reverse_diagonals.append([arr[i][d - i] for i in range(len(arr)) if 0 <= d - i < len(arr[0])])

    # Count matches in diagonals
    count = 0
    for diag in diagonals + reverse_diagonals:
        for i in range(len(diag) - word_length + 1):
            string = "".join(diag[i:i + word_length])
            if string in words:
                count += 1
    return count


def extract_xmas(param=None):
    if param:
        data = param
    else:
        data = extract_data_from_file()

    arr = create_2d_array(data)
    words = ["XMAS", "SAMX"]
    word_length = 4

    row_wise_count = get_row_wise_count(arr, words, word_length)
    column_wise_count = get_column_wise_count(arr, words, word_length)
    diagonal_wise_count = get_diagonal_wise_count(arr, words, word_length)

    total_count = row_wise_count + column_wise_count + diagonal_wise_count
    print(f"Total count of XMAS: {total_count}")
    return total_count


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
    extract_xmas()
