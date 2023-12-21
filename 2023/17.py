# Advent of code 2023
# Day 17
# Dijkstra's algorithm
# New for me. Implementing from other's solutions to learn new algorithm
# Source: Oliver-ni, hyper-neutrino
# TODO: Recreate with neighbors function
import io
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(grid, start, end, max_run):
    seen = set()
    queue = [(0, *start, 0, 0, 0)] # (heat_loss, (i,j), (dr, dc), run)
    while queue:
        hl, i, j, dr, dc, run = heappop(queue)
        if (i,j) == end:
            return hl
        # if (i,j) not in grid:
        #     continue
        if ((i,j), (dr, dc), run) in seen:
            continue
        seen.add(((i,j), (dr, dc), run))

        if run < max_run and (dr, dc) != (0, 0):
            nr = i + dr
            nc = j + dc
            if (nr, nc) in grid:
                heappush(queue, (hl + grid[(nr, nc)], nr, nc, dr, dc, run + 1))

        for dr2, dc2 in ((1,0), (0,1), (-1,0), (0,-1)):
            if (dr2, dc2) != (dr, dc) and (dr2, dc2) != (-dr, -dc):
                nr = i + dr2
                nc = j + dc2
                if (nr, nc) in grid:
                    heappush(queue, (hl + grid[(nr, nc)], nr, nc, dr2, dc2, 1))


def p1(f):
    lines = f.read().strip().splitlines()
    grid = {(i,j): int(c) for i, line in enumerate(lines) for j, c in enumerate(line)}
    n, m = len(lines), len(lines[0])
    return dijkstra(grid, (0, 0), (n-1, m-1), 3)


def dijkstra2(grid, start, end, max_run):
    seen = set()
    queue = [(0, *start, 0, 0, 0)] # (heat_loss, (i,j), (dr, dc), run)
    while queue:
        hl, i, j, dr, dc, run = heappop(queue)
        if (i,j) == end and run >= 4:
            return hl
        # if (i,j) not in grid:
        #     continue
        if ((i,j), (dr, dc), run) in seen:
            continue
        seen.add(((i,j), (dr, dc), run))

        if run < max_run and (dr, dc) != (0, 0):
            nr = i + dr
            nc = j + dc
            if (nr, nc) in grid:
                heappush(queue, (hl + grid[(nr, nc)], nr, nc, dr, dc, run + 1))

        if run >= 4 or (dr, dc) == (0, 0):
            for dr2, dc2 in ((1,0), (0,1), (-1,0), (0,-1)):
                if (dr2, dc2) != (dr, dc) and (dr2, dc2) != (-dr, -dc):
                    nr = i + dr2
                    nc = j + dc2
                    if (nr, nc) in grid:
                        heappush(queue, (hl + grid[(nr, nc)], nr, nc, dr2, dc2, 1))

def p2(f):
    lines = f.read().strip().splitlines()
    grid = {(i,j): int(c) for i, line in enumerate(lines) for j, c in enumerate(line)}
    n, m = len(lines), len(lines[0])
    return dijkstra2(grid, (0, 0), (n-1, m-1), 10)


example = io.StringIO("""
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""")

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
