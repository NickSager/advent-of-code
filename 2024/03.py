# Advent of code 2024
# Day 03
import io
import re


def p1(f):
    match = re.findall(r"mul\((\d+),(\d+)\)", f.read())
    return (sum(int(a)*int(b) for a,b in match))


def p2(f):
    match = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", f.read())
    ret = 0
    add = True

    for a,b,c,d in match:
        if d:
            add = False
        elif c:
            add = True
        elif add:
            ret += int(a) * int(b)

    return ret


example = io.StringIO("""
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".strip())
answer_1 = "161"
answer_2 = ""

example2 = io.StringIO("""
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip())

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example2))

if __name__ == '__main__':
    main()
