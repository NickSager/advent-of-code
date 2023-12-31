# Advent of code 2023
# Day 18
# Shoelace formula / Pick's theorem
import io


def p1(f):
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    points = [(0, 0)]
    boundary = 0
    
    for line in f:
        dir, dist, hex = line.split()
        dist = int(dist)
        boundary += dist
        r, c = points[-1]
        dr, dc = directions[dir]
        points.append((r + dr * dist, c + dc * dist))

    # Shoelace formula
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i + 1][1]
        area -= points[i][1] * points[i + 1][0]

    # Pick's theorem rearranged to solve for i
    # boundary added back in to adjust for border points
    return abs(area) // 2 + boundary // 2 + 1


def p2(f):
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    points = [(0, 0)]
    boundary = 0
    
    for line in f:
        dir, dist, hex = line.split()
        dir = "RDLU"[int(hex[-2])]
        dist = int(hex[2:-2], 16) # int base 16 from oliver-ni
        boundary += dist
        r, c = points[-1]
        dr, dc = directions[dir]
        points.append((r + dr * dist, c + dc * dist))

    # Shoelace formula
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i + 1][1]
        area -= points[i][1] * points[i + 1][0]

    # Pick's theorem rearranged to solve for i
    # boundary added back in to adjust for border points
    return abs(area) // 2 + boundary // 2 + 1


example = io.StringIO("""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""".strip())

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
