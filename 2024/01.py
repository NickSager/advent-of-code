# Advent of code 2024
# Day 01
from collections import defaultdict
import io


def p1(f):
    lines = f.read().strip().split('\n')
    l = [int(line.split()[0]) for line in lines]
    r = [int(line.split()[1]) for line in lines]
    merge_sort(l) #l.sort()
    merge_sort(r) #r.sort()

    return sum(abs(a-b) for a, b in zip(l,r))


def p2(f):
    lines = f.read().strip().split('\n')
    l = [int(line.split()[0]) for line in lines]
    r = [int(line.split()[1]) for line in lines]
    r_dict = defaultdict(int)

    for item in r:
        r_dict[item] += 1

    return sum(i * r_dict[i] for i in l)


# Examples of fast implementations from leader board
def p1_ans(f):
    lines = [[int(x) for x in line.split()] for line in f.read().splitlines()]
    one, two = map(sorted, zip(*lines))
    return sum(abs(a - b) for a, b in zip(one, two))


def p2_ans(f):
    lines = [[int(x) for x in line.split()] for line in f.read().splitlines()]
    one, two = map(sorted, zip(*lines))
    return sum(a * two.count(a) for a in one)


def merge_sort(arr: list[int]):
    '''
    Implementing sort to remember how. Much slower
    '''
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k+= 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr


example = io.StringIO("""
3   4
4   3
2   5
1   3
3   9
3   3
""".strip())
answer_1 = "11"
answer_2 = "31"

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
