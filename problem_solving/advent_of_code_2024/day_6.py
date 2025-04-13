"""
Link: https://adventofcode.com/2024/day/6


"""
import copy


def extract_data_from_file():
    with open("input_day_6.txt") as f:
        content = f.read()

    return content


def convert_2d_to_string(arr):
    streets = [''.join(a) for a in arr]
    area = '\n'.join(streets)
    print("@@@@@@@@@@@@@@@@@@@@")
    print(area)
    return area


def track_path(param=None):
    if not param:
        param = extract_data_from_file()
    print(param)
    rows = param.split("\n")
    data = [list(r) for r in rows]

    tracker = copy.deepcopy(data)
    guard_location = tuple()
    for idx, row in enumerate(data):
        if "^" in row:
            guard_location = (idx, row.index("^"))
            break

    i, j = None, None
    if len(guard_location):
        i, j = guard_location

    mover_axis = "i"
    direction = "up"
    count = 1
    if i and j:
        while True:
            try:
                if i >= 0 and j >= 0:
                    obstacle = data[i][j]
                else:
                    break
            except IndexError:
                break

            temp = convert_2d_to_string(tracker)
            if obstacle in [".", "X", "^"]:
                tracker[i][j] = 'X'
            elif obstacle == '#':
                if count == 1:
                    mover_axis = "j"
                    direction = "up"
                    i += 1
                    count += 1
                elif count == 2:
                    mover_axis = "i"
                    direction = "down"
                    j -= 1
                    count += 1
                elif count == 3:
                    mover_axis = "j"
                    direction = "down"
                    i -= 1
                    count += 1
                elif count == 4:
                    mover_axis = "i"
                    direction = "up"
                    j += 1
                    count = 1

            if mover_axis == "i" and direction == "up":
                i -= 1
            elif mover_axis == "i" and direction == "down":
                i += 1
            elif mover_axis == "j" and direction == "up":
                j += 1
            elif mover_axis == "j" and direction == "down":
                j -= 1

    current_area = convert_2d_to_string(tracker)
    unique_location = 0
    for x in current_area:
        if x == 'X':
            unique_location += 1

    return unique_location


def loop_found(data, param):

    tracker = copy.deepcopy(data)
    guard_location = tuple()
    for idx, row in enumerate(data):
        if "^" in row:
            guard_location = (idx, row.index("^"))
            break

    i, j = None, None
    if len(guard_location):
        i, j = guard_location

    mover_axis = "i"
    direction = "up"
    count = 1

    loop_count = 0
    loop_found = False
    if i and j:
        while True:
            loop_count += 1

            THRESHOLD = len(param) * len(param)
            if loop_count == THRESHOLD:
                loop_found = True
                break

            try:
                if i >= 0 and j >= 0:
                    obstacle = data[i][j]
                else:
                    break
            except IndexError:
                break

            temp = convert_2d_to_string(tracker)
            if obstacle in [".", "X", "^"]:
                tracker[i][j] = 'X'
            elif obstacle == '#':
                if count == 1:
                    mover_axis = "j"
                    direction = "up"
                    i += 1
                    count += 1
                elif count == 2:
                    mover_axis = "i"
                    direction = "down"
                    j -= 1
                    count += 1
                elif count == 3:
                    mover_axis = "j"
                    direction = "down"
                    i -= 1
                    count += 1
                elif count == 4:
                    mover_axis = "i"
                    direction = "up"
                    j += 1
                    count = 1

            if mover_axis == "i" and direction == "up":
                i -= 1
            elif mover_axis == "i" and direction == "down":
                i += 1
            elif mover_axis == "j" and direction == "up":
                j += 1
            elif mover_axis == "j" and direction == "down":
                j -= 1

    return loop_found


def create_obstacle(param):
    if not param:
        param = extract_data_from_file()
    print(param)
    rows = param.split("\n")
    data = [list(r) for r in rows]

    tracker = copy.deepcopy(data)

    guard_loc = None
    for idx, row in enumerate(data):
        for idx2, pos in enumerate(row):
            if data[idx][idx2] == "^":
                guard_loc = idx

    obstacle_location = 0
    for idx, row in enumerate(data):
        for idx2, pos in enumerate(row):
            if data[idx][idx2] != "^":
                # guard_location = (idx, idx2)
                old_data = tracker[idx][idx2]
                tracker[idx][idx2] = "#"
                if loop_found(tracker, param):
                    obstacle_location += 1
                else:
                    tracker[idx][idx2] = old_data

    return obstacle_location


if __name__ == '__main__':
    input = \
"""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    input2 = \
"""....#.....
.........#
..........
....^.....
..........
.#........
..........
..........
......#...
........#."""
    # solution = track_path()
    solution = create_obstacle(input)
    1==1