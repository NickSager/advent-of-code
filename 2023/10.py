# Advent of code 2023
# Day 10
# FIX: Add Typing to clean up errors
# TODO: Find solution for pt2
# TODO: Compare better solutions, Breadth First Search?.

# Parse file
file_path = "input/10ex.txt"
coord_map = {}
with open(file_path, "r") as f:
    data = f.read().strip().split("\n")
    for y in range(len(data)):
        for x in range(len(data[y])):
            coord_map[x, y] = data[y][x]


# Solve Problem
def step(coord_map, x, y, xl, yl):
    mv_right = x > xl
    mv_up = y < yl
    mv_left = x < xl
    mv_down = y > yl

    right = (x+1, y)
    left = (x-1, y)
    up = (x, y-1)
    down = (x, y+1)

    if coord_map[x, y] == "|":
        if mv_up:
            return up
        else:
            return down
    elif coord_map[x, y] == "-":
        if mv_right:
            return right
        else:
            return left
    elif coord_map[x, y] == "L":
        if mv_down:
            return right
        else:
            return up
    elif coord_map[x, y] == "J":
        if mv_down:
            return left
        else:
            return up
    elif coord_map[x, y] == "7":
        if mv_up:
            return left
        else:
            return down
    elif coord_map[x, y] == "F":
        if mv_up:
            return right
        else:
            return down
    elif coord_map[x, y] == "S":
        if coord_map[right] in ['-', '7', 'J']:
            return right
        elif coord_map[left] in ['-', 'L', 'F']:
            return left
        elif coord_map[up] in ['|', '7', 'F']:
            return up
        elif coord_map[down] in ['|', 'J', 'L']:
            return down
    else:
        raise Exception("Invalid character in map")



def count(coord_map, x, y):
    ''' Count steps from S back to S '''
    steps = 0
    xl, yl = x, y
    while True:
        x, y, xl, yl = *step(coord_map, x, y, xl, yl), x, y
        steps += 1
        if coord_map[x, y] == "S":
            return steps

# Find S
xs, ys = [k for k, v in coord_map.items() if v == "S"][0]
count = count(coord_map, xs, ys)
apex = count // 2 + count % 2
print("Part 1:", apex)
