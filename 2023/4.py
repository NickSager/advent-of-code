# Advent of code 2023
# Day 4

import re
import fileinput

cards = {}

# Parse file
for y, line in enumerate(fileinput.input()):
    pattern = r'Card\s+(\d+):\s+(.*)\s+\|\s+(.*)'
    match = re.search(pattern, line.strip())

    if match:
        card_no = int(match.group(1))
        winners = match.group(2)
        have = match.group(3)

        winners = winners.split()
        have = have.split()
        cards[card_no] = (winners, have)

# Solve Problem
scores = {}
copies = {card: 1 for card in cards}

for card in cards:
    matches = 0
    winners, have = cards[card]
    for num in have:
        if num in winners:
            matches += 1
    if matches > 0:
        scores[card] = 1 * 2 ** (matches-1)
        for i in range(matches):
            next = card + i + 1
            if next in copies:
                copies[next] += copies[card]
    else:
        scores[card] = 0

print("Part 1:", sum(scores[i] for i in scores))
print("Part 2:", sum(copies[i] for i in copies))
