def rec_approach(data, new_data=None):
    if new_data is None:
        new_data = {}
    for key, value in data.items():
        if isinstance(value, dict) and value is not None:
            new_data[key] = rec_approach(value, {})
            continue
        else:
            if value is not None:
                new_data[key] = value
    return new_data


if __name__ == '__main__':
    data = {
    'a': 1,
    'b': None,
    'c': {
        'd': 2,
        'e': None,
        'f': {
            'g': None,
            'h': 3
        }
    }
}

    res = rec_approach(data)
    1==1