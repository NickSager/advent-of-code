# Advent of code 2024
# Day 05
import io
from collections import defaultdict


def p1(f):
    rules, lists = f.read().split("\n\n")
    ruledict = defaultdict(list)
    count = 0

    [(ruledict[int(a)].append(int(b))) for line in rules.split('\n')
        for a, b in [line.split("|")] if line]

    for l in lists.splitlines():
        nums = [int(x) for x in l.split(",")]
        valid = True
        for i in range(len(nums)):
            if any(rule in nums[:i] for rule in ruledict[nums[i]]):
                valid = False
                break
        if valid:
            count += nums[len(nums) // 2]

    return count


def p2(f):
    rules, lists = f.read().split("\n\n")
    ruledict = defaultdict(list)
    invalid = []
    count = 0

    [(ruledict[int(a)].append(int(b))) for line in rules.split('\n')
        for a, b in [line.split("|")] if line]

    for l in lists.splitlines():
        nums = [int(x) for x in l.split(",")]
        valid = True
        for i in range(len(nums)):
            if any(rule in nums[:i] for rule in ruledict[nums[i]]):
                valid = False
                invalid.append(nums)
                break

    for l in invalid:
        sorted_list = l.copy()
        wrong = True

        while wrong:
            wrong = False
            for i in range(len(sorted_list) - 1):
                a, b = sorted_list[i], sorted_list[i + 1]
                if b in ruledict[a]:
                    sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                    wrong = True

        count += sorted_list[len(sorted_list) // 2]

    return count


# From leaderboard. Stable sorting allows this to work but slow. Elegant
from functools import cmp_to_key

def p2_ans(f):
    os, ls = [x.splitlines() for x in f.read().split("\n\n")]
    os = [[int(x) for x in o.split("|")] for o in os]
    ls = [[int(x) for x in o.split(",")] for o in ls]
    ans = 0
    for nums in ls:
        for x, y in os:
            try:
                if nums.index(x) >= nums.index(y):
                    break
            except ValueError:
                pass
        else:
            continue
        nums.sort(key=cmp_to_key(lambda x, y: -([x, y] in os) + ([y, x] in os)))
        ans += nums[len(nums) // 2]
    return ans

example = io.StringIO("""
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip())
answer_1 = "143"
answer_2 = "123"

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
