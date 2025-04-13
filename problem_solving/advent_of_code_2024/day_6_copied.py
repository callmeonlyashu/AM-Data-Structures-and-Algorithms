

def find_caret(map):
    y = 0
    for line in map:
        if '^' in line:
            x = line.find('^')
            return (x, y)
        y += 1

    print('caret not found')
    exit()


def turn_right(direction):
    if direction == (-1, 0):
        return (0, -1)
    if direction == (0, -1):
        return (1, 0)
    if direction == (1, 0):
        return (0, 1)
    if direction == (0, 1):
        return (-1, 0)
    print('invalid direction')
    exit()


def guard_on_map(map, position):
    width = len(map[0])
    height = len(map)
    if position[0] < 0 or position[1] < 0:
        return False
    if position[0] >= width:
        return False
    if position[1] >= height:
        return False
    return True


def mark_guard_position(map, position):
    add_char_to_map(map, position, 'X')


def add_obstacle_to_map(map, position):
    add_char_to_map(map, position, '#')


def add_char_to_map(map, position, char):
    line = map[position[1]]
    char_list = list(line)
    if char_list[position[0]] == '#' and char != '#':
        print("Uh-ohhh, you're overwriting a barrier")
        exit()
    if char_list[position[0]] == '^' and char == '#':
        print("Uh-ohhh, you're overwriting the carrot")
        exit()
    char_list[position[0]] = char
    map[position[1]] = ''.join(char_list)


def new_position(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])


def guard_facing_obstacle(map, pos, dir):
    new_pos = new_position(pos, dir)
    try:
        if map[new_pos[1]][new_pos[0]] == '#':
            return True
    except IndexError:
        pass
    return False


def loop_detected(map, pos, dir):
    # we start following the path until we either
    # revisit a position, in which case we found a loop
    # or we go off the board, in which case there
    # is no loop
    position_history = set()  # records position and direction

    while guard_on_map(map, pos):
        if pos + dir in position_history:
            return True
        position_history.add(pos + dir)
        if guard_facing_obstacle(map, pos, dir):
            dir = turn_right(dir)
        else:
            pos = new_position(pos, dir)

    return False

# from lib import find_caret, turn_right, guard_on_map, \
#     new_position, guard_facing_obstacle, add_obstacle_to_map, loop_detected

with open('input_day_6.txt', 'r') as f:
    data = f.read()

map = data.split('\n')

# This will hold a record of every position the guard will occupy
# and the direction they were going when in that position
position_history = set()

caret_position = find_caret(map)
guard_position = caret_position
direction = (0, -1)

# first we create a record of all the positions the
# guard will occupy on the normal route.
while guard_on_map(map, guard_position):

    if guard_position != caret_position:  # we can't put an obstacle in the original guard position
        position_history.add(guard_position)

    if guard_facing_obstacle(map, guard_position, direction):
        direction = turn_right(direction)
    else:
        guard_position = new_position(guard_position, direction)

# go through the position history and try placing an obstacle
# in each location to see if it results in a loop
positions_causing_loops = []

for position in position_history:
    new_map = map[:]
    add_obstacle_to_map(new_map, position)
    if loop_detected(new_map, caret_position, (0, -1)):
        positions_causing_loops.append(position)

print(len(positions_causing_loops))
