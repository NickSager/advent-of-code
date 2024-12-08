# Advent of code 2024
# Day 06
import io


def p1(f):
    lines = f.read().strip().splitlines()
    grid = {(i,j): (c) for i, line in enumerate(lines) for j, c in enumerate(line)}
    ROWS = max(pos[0] for pos in grid.keys())
    COLS = max(pos[1] for pos in grid.keys())
    dir_order = ["^", ">", "v", "<"]
    dirs = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}

    curr, dir = next(((pos, val) for pos, val in grid.items() if val in dirs), (None, None))
    if curr is None:
        return "No starting point found"
    visit = set()

    delta = dirs[dir]
    nxt = (curr[0] + delta[0], curr[1] + delta[1])

    while 0 <= nxt[0] <= ROWS and 0 <= nxt[1] <= COLS:
        if grid[nxt] == "#":
            current_idx = dir_order.index(dir)
            dir = dir_order[(current_idx + 1) % 4]
            nxt = (curr[0] + dirs[dir][0], curr[1] + dirs[dir][1])
            continue
        visit.add(curr)
        curr = nxt
        nxt = (curr[0] + dirs[dir][0], curr[1] + dirs[dir][1])

    visit.add(curr)
    return len(visit)


def p2(f):
    lines = f.read().strip().splitlines()
    grid = {(i,j): (c) for i, line in enumerate(lines) for j, c in enumerate(line)}
    ROWS = max(pos[0] for pos in grid.keys())
    COLS = max(pos[1] for pos in grid.keys())
    dir_order = ["^", ">", "v", "<"]
    dirs = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}
    count = 0

    # Modify each square and add count if there is cycle
    for pos, val in grid.items():
        grid2 = grid.copy()
        if val in dir_order:
            continue
        grid2[pos] = "#"
        curr, dir = next(((pos, val) for pos, val in grid2.items() if val in dirs), (None, None))
        if curr is None:
            return "No starting point found"
        visit = set()

        delta = dirs[dir]
        nxt = (curr[0] + delta[0], curr[1] + delta[1])

        while 0 <= nxt[0] <= ROWS and 0 <= nxt[1] <= COLS:
            if grid2[nxt] == "#":
                current_idx = dir_order.index(dir)
                dir = dir_order[(current_idx + 1) % 4]
                nxt = (curr[0] + dirs[dir][0], curr[1] + dirs[dir][1])
                continue
            if (curr, dir) in visit:
                count += 1
                break
            visit.add(( curr, dir ))
            curr = nxt
            nxt = (curr[0] + dirs[dir][0], curr[1] + dirs[dir][1])

        # visit.add(curr)
    return count


# Much better way to do this without repeated work.
# Can avoid separate class with dr, dc = dc, -dr rotation
def sim(grid, pos, dir):
    visited = set()
    while pos in grid:
        if (pos, dir) in visited:
            return True, visited
        visited.add((pos, dir))
        while grid.get(pos + dir, ".") == "#":
            dir = dir.rot()
        pos += dir
    return False, visited


# example = io.StringIO("""
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """.strip())
answer_1 = ""
answer_2 = ""

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
