# Advent of code 2023
# Day 13

def check_smudge(a, b):
    if len(a) != len(b):
        raise ValueError("Lengths don't match")

    return sum(1 for i in range(len(a)) if a[i] != b[i])


def check_row(block):
    lines = block.split('\n')
    for i in range(len(lines) - 1):
        if lines[i+1] == lines[i]:
            b, f = i, i+1
            while b >= 0 and f < len(lines):
                if lines[b] != lines[f]:
                    break
                b -= 1
                f += 1
            if b < 0 or f >= len(lines):
                return i+1

    return 0

def check_col(block):
    lines = block.split('\n')

    # Transpose to avoid column issues
    transpose = [''.join(x) for x in zip(*lines)]
    transpose_block = '\n'.join(transpose)

    return check_row(''.join(transpose_block))

def p1(f):
    total = 0
    blocks = f.read().split('\n\n')
    for block in blocks:
        total += 100 * check_row(block)
        total += check_col(block)

    return total

# Upon further inspection, adapting my part 1 method is ugly and
# doesn't handle smudges at the reflection. Adopting oliver's solution
# for practice. Much simpler and more powerful.
# NOTE: Walrus operator!
def p2(f):
    total = 0
    blocks = f.read().split('\n\n')

    def find(block):
        for i in range(1, len(block)):
            differs = sum(
                ax != bx
                for a, b in zip(block[:i][::-1], block[i:])
                for ax, bx in zip(a, b)
            )
            if differs ==1:
                return i

    for block in blocks:
        block = block.split('\n')
        if v:= find([*zip(*block)]):
            total += v
        if h:= find(block):
            total += h * 100

    return total

# For debugging purposes
def main():
    print(p1(example))
    print(p2(example))

if __name__ == '__main__':
    main()

example = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip()
