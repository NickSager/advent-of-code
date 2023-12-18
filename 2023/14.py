# Advent of code 2023
# Day 14
import io

def move(row):
    # Move O's to the left of a row
    w = 0
    for i in range(len(row)):
        if row[i] == 'O':
            row[i], row[w] = row[w], row[i]
            w += 1
            while w < len(row) and row[w] == '#':
                w += 1
        elif row[i] == '#':
            w = i+1

def p1(f):
    total = 0
    rows = f.read().strip().split('\n')

    rows_t = [list(row) for row in zip(*rows)]
    for row in rows_t:
        move(row)
        # print(row, end='\n')
        total += sum((row[i] == "O")*(len(row)-i) for i in range(len(row)))
    return total

def p2(f):
    total = 0
    rows = f.read().strip().split('\n')

    num_cycles = 1000000000
    count = 0
    seen = {tuple(tuple(row) for row in rows): 0}
    cycle = False

    while count < num_cycles:
        for _ in range(4):
            rows = [list(row) for row in zip(*rows)]
            for row in rows:
                move(row)
            rows = [row[::-1] for row in rows] # Reversing -> clockwise 90

        count += 1

        if tuple(tuple(row) for row in rows) in seen and not cycle:
            print(f"Found repeat at {count}")
            cycle = count - seen[tuple(tuple(row) for row in rows)]
            count += (num_cycles - count) // cycle * cycle
            if count == num_cycles:
                break

        seen[tuple(tuple(row) for row in rows)] = count

        # Optional print debugging
        # print('-'*10)
        # for row in rows:
        #     print(row, end='\n')

    rows = [list(row) for row in zip(*rows)]
    for row in rows:
        total += sum((row[i] == "O")*(len(row)-i) for i in range(len(row)))
    return total

example = io.StringIO("""
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""")  #.strip()

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
