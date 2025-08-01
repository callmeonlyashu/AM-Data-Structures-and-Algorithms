
def char_occurrence(str):
    count_char_dict = {}
    for i in str:
        if i not in count_char_dict:
            count_char_dict[i] = 1
        else:
            count_char_dict[i] += 1

    max = 0
    second_max = 0
    result_key = None
    for key, value in count_char_dict.items():
        if value > max:
            max = value
        if max > value > second_max:
            second_max = value
            result_key = key

    return result_key


if __name__ == '__main__':
    str = "aaaaaaaaa bbbb dddddd cc ggggggg"
    char = char_occurrence(str)