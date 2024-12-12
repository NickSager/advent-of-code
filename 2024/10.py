# Advent of code 2024
# Day 10
import io


def dfs(r, c, val, grid, visit, nines):
    if (r,c) not in grid or (r,c) in visit:
        return 0

    if grid[(r,c)] != (val + 1):
        return 0

    if grid[(r,c)] == 9:
        nines.add((r,c))
        return 1

    visit.add((r,c))
    count = 0
    for dr, dc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
        count += dfs(dr, dc, grid[(r,c)], grid, visit, nines)
    visit.remove((r,c))
    return count


def p1(f):
    lines = f.read().strip().splitlines()
    grid = {(i,j): int(c) for i, line in enumerate(lines) for j, c in enumerate(line)}

    starts = [key for key, val in grid.items() if val == 0]
    count = 0
    for start in starts:
        visit = set()
        nines = set()
        dfs(*start, -1, grid, visit, nines)
        count += len(nines)

    return count


def p2(f):
    lines = f.read().strip().splitlines()
    grid = {(i,j): int(c) for i, line in enumerate(lines) for j, c in enumerate(line)}

    starts = [key for key, val in grid.items() if val == 0]
    count = 0
    for start in starts:
        visit = set()
        nines = set()
        count += dfs(*start, -1, grid, visit, nines)
        # count += len(nines)

    return count


# Cleaner solution implemented for practice
# Generator DFS
class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def rot(self):
        x, y = self
        return T((y, -x))

NORTH = T((-1, 0))
EAST = NORTH.rot()
SOUTH = EAST.rot()
WEST = SOUTH.rot()

def find(grid, p):
    if grid[p] == 9:
        yield [p]
    for dir in (NORTH, EAST, SOUTH, WEST):
        if grid.get(p + dir, -1) == grid[p] + 1:
            for thing in find(grid, p + dir):
                yield [p, *thing]

def p1_ans(f):
    grid = {
        T((i, j)): int(c)
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }
    starts = [p for p, c in grid.items() if c == 0]
    return sum(len({path[-1] for path in find(grid, p)}) for p in starts)

def p2_ans(f):
    grid = {
        T((i, j)): int(c)
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }
    starts = [p for p, c in grid.items() if c == 0]
    return sum(1 for p in starts for _ in find(grid, p))

example = io.StringIO("""
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip())
answer_1 = "36"
answer_2 = "81"

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
