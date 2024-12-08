# Advent of code 2024
# Day 02
import io


def p1(f):
    lines = f.read().split('\n')
    count = 0

    for line in lines:
        levels = line.split()
        diffs = []
        for i in range(1,len(levels)):
            diffs.append(int(levels[i]) - int(levels[i-1]))
        if abs(max(diffs)) > 3 or abs(min(diffs)) > 3:
            continue
        elif max(diffs) >= 0 and min(diffs) <= 0:
            continue
        count += 1

    return count


# Two pointer method will not work because the skip that makes this work
# is not necessarily where the fault is detected. Interesting.
def p2(f):
    lines = f.read().split('\n')
    count = 0

    for line in lines:
        levels = [int(x) for x in line.split()]
        diffs = [0] * (len(levels) - 1)
        j = 0
        fault = 0

        for i in range(len(levels)-1):
            diff = levels[i+1] - levels[j]
            if abs(diff) > 3 or diff == 0:
                fault += 1
                if fault > 1:
                    break
                continue
            elif j > 0 and diff * diffs[j-1] < 0:
                fault += 1
                if fault > 1:
                    break
                continue
            diffs[j] = diff
            j += 1

        if fault <= 1 and j >= len(levels)-2:
            count += 1

    return count # 337


# Brute force list slicing form leaderboard
def safe(levels):
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)

def p2_ans(f):
    lines = f.read().split('\n')
    count = 0

    for report in lines:
        levels = list(map(int, report.split()))
        if any(safe(levels[:index] + levels[index + 1:]) for index in range(len(levels))):
            count += 1

    return count



example = io.StringIO("""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip())

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
