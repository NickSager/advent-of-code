# Advent of code 2024
# Day 04
import io


def p1(f):
    grid = f.read().split('\n')
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "X":
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if r + 3*dr < len(grid) and r + 3*dr > -1:
                            if c + 3*dc < len(grid[0]) and c + 3*dc > -1:
                                if grid[r+1*dr][c+1*dc] == "M" and grid[r+2*dr][c+2*dc] == "A" and grid[r+3*dr][c+3*dc] == "S":
                                    count += 1

    return count


def p2(f):
    grid = f.read().split('\n')
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "A":
                for dr in [-1, 1]:
                    for dc in [-1, 1]:
                        if r + dr < len(grid) and r + dr > -1 and r - dr < len(grid) and r - dr > -1:
                            if c + dc < len(grid[0]) and c + dc > -1 and c - dc < len(grid[0]) and c - dc > -1:
                                if ((grid[r+dr][c+dc] == "M" and grid[r-dr][c-dc] == "S" and grid[r-dr][c+dc] == "M" and grid[r+dr][c-dc] == "S") 
                                        or (grid[r+dr][c+dc] == "M" and grid[r-dr][c-dc] == "S" and grid[r-dr][c+dc] == "S" and grid[r+dr][c-dc] == "M")):
                                    count += 1

    return ( count//2 )

# Cleaner answer
def p2_ans(f):
    grid = f.read().splitlines()
    count = 0

    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if grid[r][c] != "A": continue
            corners = [grid[r - 1][c - 1], grid[r - 1][c + 1], grid[r + 1][c + 1], grid[r + 1][c - 1]]
            if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                count += 1

    return (count)

example = io.StringIO("""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip())
answer_1 = "18"
answer_2 = "9"

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
