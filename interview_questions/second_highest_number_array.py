def second_highest(list_items):
    max_value = None
    second_max = None

    for value in list_items:
        if max_value is None or value > max_value:
            second_max = max_value
            max_value = value
        elif second_max is None or second_max < value < max_value:
            second_max = value

    return second_max


if __name__ == '__main__':
    list_items = [3, 5, 6, 9, 11]
    char = second_highest(list_items)
    1==1