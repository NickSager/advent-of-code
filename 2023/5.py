# Advent of code 2023
# Day 5
import re

# Parse file
file_path = 'input/5.txt'
with open(file_path, 'r') as f:
    content = f.read()

    blocks = re.split(r'\n\n', content)
    data = {}

    for i in range(len(blocks)):
        key, values = re.split(r':', blocks[i])
        if key == 'seeds':
            data[key] = [int(x) for x in values.split()]
        else:
            data[key] = [[int(x) for x in match.groups()] for match in re.finditer(r'(\d+)\s+(\d+)\s+(\d+)', values)]


# Part 1
locations = {}

for seed in data['seeds']:
    locations[seed] = seed
    for key, value in list(data.items())[1:]:
        for item in value:
            if locations[seed] >= item[1] and locations[seed] < item[1] + item[2]:
                locations[seed] = locations[seed] - item[1] + item[0]
                break

print("Part 1:", min(locations.values()))

# Part 2, parse seeds
seeds = data['seeds']
seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
seeds = [range(s, s+r) for (s, r) in seeds]

for key, value in list(data.items())[1:]:
    mappings = [(range(dest, dest+length), range(source, source+length)) for dest, source, length in value]
    adj_seeds = []

    for seed in seeds:
        for dest, source in mappings:
            offset = dest.start - source.start
            if seed.stop <= source.start or seed.start >= source.stop:
                continue
            inner_range = range(max(seed.start, source.start), min(seed.stop, source.stop))
            left_range = range(seed.start, inner_range.start)
            right_range = range(inner_range.stop, seed.stop)
            if left_range:
                seeds.append(left_range)
            if right_range:
                seeds.append(right_range)
            adj_seeds.append(range(inner_range.start + offset, inner_range.stop + offset))
            break
        else:
            adj_seeds.append(seed)
    seeds = adj_seeds
ans = min([s.start for s in seeds])
print("Part 2:", min([s.start for s in seeds]))
