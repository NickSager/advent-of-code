# Advent of code 2023
# Day 16
# Deque and match-case adopted from oliver-ni. Nicer than if-elif
import io
from collections import deque

def energize(data, start = [(0, -1, 0, 1)]):
    seen = set()
    queue = deque(start)

    while queue:
        r, c, dr, dc = queue.popleft()
        r += dr
        c += dc

        if (r, c, dr, dc) in seen:
            continue
        if r >= len(data) or r < 0 or c >= len(data[0]) or c < 0:
            continue
        seen.add((r, c, dr, dc))
        match data[r][c]:
            case '/':
                dr, dc = -dc, -dr
            case '\\':
                dr, dc = dc, dr
            case '|' if dr == 0: 
                queue.append((r, c, 1, 0))
                queue.append((r, c, -1, 0))
                continue
            case '-' if dc == 0: 
                queue.append((r, c, 0, 1))
                queue.append((r, c, 0, -1))
                continue
            case _:
                pass
        queue.append((r, c, dr, dc))

    return len(set((r, c) for (r, c, _, _) in seen))


def p1(f):
    data = f.read().strip().split('\n')

    return energize(data)

def p2(f):
    total = 0
    data = f.read().strip().split('\n')

    for i in range(len(data)):
        total = max(total, energize(data, [(i, -1, 0, 1)]))
        total = max(total, energize(data, [(i, len(data[0]), 0, -1)]))
    for i in range(len(data[0])):
        total = max(total, energize(data, [(-1, i, 1, 0)]))
        total = max(total, energize(data, [(len(data), i, -1, 0)]))

    return total

# Manually escaped the backslashes
example = io.StringIO("""
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
""")

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
