# Advent of code 2023
# Day 6

import re
import math

# Parse file
file_path = 'input/6.txt'
games = {}
with open(file_path, 'r') as f:
    content = f.read()

    blocks = re.split(r'\n', content.strip())
    data = {}

    # Process Each Row
    for i in range(len(blocks)):
        key, values = re.split(r':', blocks[i])
        data[key] = [int(x) for x in values.split()]

    # Change rows into a dict of games
    for i, v in enumerate(data['Time']):
        games[i] = [v, data['Distance'][i]]

# Solve Problem
def calc_dist(hold, total):
    return hold * (total - hold)

def calc_wins(time, dist):
    wins = 0
    for i in range(1, time):
        curr = calc_dist(i, time)
        if curr > dist:
            wins += 1
    return wins

print("Part 1:", math.prod([calc_wins(val[0],val[1]) for val in games.values()]))

# Part 2
time = int(''.join(map(str, [game[0] for game in games.values()])))  # Help from GPTF-4 for concantenation
distance = int(''.join(map(str, [game[1] for game in games.values()])))

print("Part 2:", calc_wins(time, distance))
