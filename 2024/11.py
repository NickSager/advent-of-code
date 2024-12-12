# Advent of code 2024
# Day 11
import io
from functools import cache # Easier memoization


@cache
def transform(stone, steps):
    if steps == 0:
        return 1
    if stone==0:
        return transform(1, steps-1)
    elif len(str(stone)) % 2 ==0:
        half = len(str(stone)) // 2
        return transform(int(str(stone)[:half]), steps -1) + \
            transform(int(str(stone)[half:]), steps-1)
    else:
        return transform(stone * 2024, steps-1)


def p1(f):
    line = [int(x) for x in f.read().split()]
    # Transform originally done this way for part one. No steps
    # for _ in range(75):
    #     newline = []
    #     for stone in line:
    #         newline.extend(transform(stone, 1))
    #     line = newline

    # return len(line)
    return sum(transform(stone, 25) for stone in line)


def p2(f):
    line = [int(x) for x in f.read().split()]
    return sum(transform(stone, 75) for stone in line)


example = io.StringIO("""
125 17
""".strip())
answer_1 = "55312"
answer_2 = ""

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
