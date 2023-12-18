# Advent of code 2023
# Day 8

import re
from math import lcm

maps = {}

# Parse file
file_path = 'input/8.txt'
with open(file_path, 'r') as f:
    data = f.read().strip()
    moves, *nodes = data.split('\n')

    pattern = r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)'
    for node in nodes:
        match = re.search(pattern, node)
        if match:
            maps[match.group(1)] = (match.group(2), match.group(3))
        else:
            print("No match", node)


def next(node, direction):
    if direction == 'L':
        return maps[node][0]
    elif direction == 'R':
        return maps[node][1]
    else:
        print("Unknown direction", direction)

# Solve Problem
pt_1 = 0
node = 'AAA'  # Start node
while node != 'ZZZ':
    node = next(node, moves[pt_1 % len(moves)])
    pt_1 += 1
print("Part 1:", pt_1)

# Solution adopted from several users on leaderboard (eg. oliver-ni)
# Since the problem says there are cycles, we can calculate the cycle length
# for each, and find the least common multiple of the cycle lengths
# Chinese Remainder Theorem
pt_2 = 0
counts = []
nodes = [node for node in maps.keys() if node[2]=='A']
while nodes:
    move = moves[pt_2 % len(moves)]
    for i, node in enumerate(nodes):
        nodes[i] = next(node, move)
        if nodes[i][-1] == 'Z':
            counts.append(pt_2+1)
    nodes = [node for node in nodes if not node[-1] == 'Z']
    pt_2 += 1
print("Part 2:", lcm(*counts))
