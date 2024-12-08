# Advent of code 2024
# Day 08
import io


def p1(f):
    lines = f.read().strip().splitlines()
    grid = {(i,j): [c] for i, line in enumerate(lines) for j, c in enumerate(line)}
    ROWS = max(pos[0] for pos in grid.keys())
    COLS = max(pos[1] for pos in grid.keys())

    # Populate antinodes
    nodes = [(pos, val[0]) for pos, val in grid.items() if '.' not in val]
    for pos, val in nodes:
        for pos2, val2 in nodes:
            if pos == pos2: continue
            if val != val2: continue
            dr, dc = pos2[0]-pos[0], pos2[1]-pos[1]
            new = (pos2[0]+dr, pos2[1]+dc)
            if new in grid:
                grid[new].append("#")

    # for r in range(ROWS+1):
    #     for c in range(COLS+1):
    #         if "#" in grid[r,c]:
    #             print("#", end="")
    #         else: print(grid[r,c][0], end="")
    #     print()

    # Count anti-nodes
    return sum(("#" in c) for c in grid.values())


def p2(f):
    lines = f.read().strip().splitlines()
    grid = {(i,j): [c] for i, line in enumerate(lines) for j, c in enumerate(line)}
    ROWS = max(pos[0] for pos in grid.keys())
    COLS = max(pos[1] for pos in grid.keys())

    # Populate antinodes
    nodes = [(pos, val[0]) for pos, val in grid.items() if '.' not in val]
    for pos, val in nodes:
        for pos2, val2 in nodes:
            if pos == pos2: continue
            if val != val2: continue
            dr, dc = pos2[0]-pos[0], pos2[1]-pos[1]
            new = (pos[0]-dr, pos[1]-dc)
            new2 = (pos2[0]+dr, pos2[1]+dc)
            grid[pos].append("#")
            while new in grid:
                grid[new].append("#")
                new = (new[0]-dr, new[1]-dc)
            while new2 in grid:
                grid[new2].append("#")
                new2 = (new2[0]+dr, new2[1]+dc)


    # for r in range(ROWS+1):
    #     for c in range(COLS+1):
    #         if "#" in grid[r,c]:
    #             print("#", end="")
    #         else: print(grid[r,c][0], end="")
    #     print()

    # Count anti-nodes
    return sum(("#" in c) for c in grid.values())


example = io.StringIO("""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip())
answer_1 = ""
answer_2 = "34"

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
