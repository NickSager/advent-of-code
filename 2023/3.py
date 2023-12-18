# Advent of code 2023
# Day 3
# Adopted from iKevinY's solution

# Parse file
symbols = {}
parts = []

with open('2023/input/3_ex.txt', 'r') as f:
    for r, line in enumerate(f.read().splitlines()):
        part = ''
        start = None
        for c, char in enumerate(line):
            match char:
                case char if char.isdigit():
                    if not part: #Start new part number
                        start = c
                    part += char
                case _:
                    if part: # end current part number
                        parts.append((int(part), r, start, c-1))
                        part = ''
                    if char != '.': # add symbol
                        symbols[c, r] = char

        if part:
            parts.append((int(part), r, start, len(line)-1))


# Solve Problem
seen = set()
part_2 = 0

for c, r in symbols:
    adjacent = []
    for (part, row, start, end) in parts:
        if row - 1 <= r <= row + 1 and start - 1 <= c <= end + 1:
            seen.add(part)
            adjacent.append(part)

    if len(adjacent) == 2 and symbols[c, r] == '*':
        part_2 += adjacent[0] * adjacent[1]

print("Part 1:", sum(seen))
print("Part 2:", part_2)
