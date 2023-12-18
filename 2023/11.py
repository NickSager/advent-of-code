# Advent of code 2023
# Day 11

from itertools import combinations

def expand_universe(universe):
    new = []
    # Double empty rows
    for line in universe:
        new.append(line)
        if all(char == '.' for char in line):
            new.append(line)

    # Transpose to avoid column issues -GPT-4
    transpose = [''.join(x) for x in zip(*new)]

    # Double empty columns (rows)
    new2 = []
    for line in transpose:
        new2.append(line)
        if all(char == '.' for char in line):
            new2.append(line)

    # Transpose back
    expanded = [''.join(x) for x in zip(*new2)]
    return expanded

# Parse file
file_path = "input/11.txt"
universe = {}
with open(file_path, "r") as f:
    data = f.read().strip().split("\n")
    data = expand_universe(data)
    for y in range(len(data)):
        for x in range(len(data[y])):
            universe[x, y] = data[y][x]

# Solve Problem
galaxies = [g for g in universe if universe[g] == "#"]
galaxies = {i: galaxy for i, galaxy in enumerate(galaxies, start=1)}
pairings = list(combinations(galaxies.keys(), 2))

def get_distance(x1, y1, x2, y2):
    #Integer shortest path distance
    return abs(x1-x2) + abs(y1-y2)

distance = sum([get_distance(*galaxies[pair[0]], *galaxies[pair[1]]) for pair in pairings])
print("Part 1:", distance)

# Part 2
# My solution will not work for part 2.
# Instead, solving it by counting the empty rows crossed and adding scaled distance
# Adopded from oliver-ni. Also doing away with dictionary

with open(file_path, "r") as f:
    data = f.read().strip().split("\n")

# Solve Problem
empty_x = {y for y, line in enumerate(data) if '#' not in line}
empty_y = {x for x in range(len(data[0])) if not any(line[x] == '#' for line in data)}
galaxies = {(x,y) for y, line in enumerate(data) for x, char in enumerate(line) if char == '#'}

distance = sum(
    abs(p[0] - q[0]) +
    abs(p[1] - q[1]) +
    999999 * len(empty_x.intersection(range(min(p[1], q[1]), max(p[1], q[1])))) +
    999999 *len(empty_y.intersection(range(min(p[0], q[0]), max(p[0], q[0]))))
    for p, q in combinations(galaxies, 2)
)
print("Part 2:", distance)
