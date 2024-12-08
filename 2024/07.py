# Advent of code 2024
# Day 07
import io

# Help from leaderboard on this recursion. My brute force timed out.
def test(ans, nums):
    if len(nums) == 1:
        return nums[0] == ans
    if ans % nums[-1] == 0 and test(ans // nums[-1], nums[:-1]):
        return True
    if test(ans - nums[-1], nums[:-1]):
        return True
    return False


def test2(ans, nums):
    if len(nums) == 1:
        return nums[0] == ans
    if ans % nums[-1] == 0 and test2(ans // nums[-1], nums[:-1]):
        return True
    if ans > nums[-1] and test2(ans - nums[-1], nums[:-1]):
        return True
    # Recursive concatenation check from HN
    s_target = str(ans)
    s_last = str(nums[-1])
    if s_target.endswith(s_last) and len(s_target) > len(s_last) and test2(int(s_target[:-len(s_last)]), nums[:-1]):
        return True
    return False


def p1(f):
    lines = f.read().strip().splitlines()
    ans = [int(line.split(": ")[0]) for line in lines]
    nums = [[int(n) for n in line.split(": ")[1].split()] for line in lines]
    total = 0

    for i in range(len(ans)):
        if test(ans[i], nums[i]):
            total += ans[i]

    return total


def p2(f):
    lines = f.read().strip().splitlines()
    ans = [int(line.split(": ")[0]) for line in lines]
    nums = [[int(n) for n in line.split(": ")[1].split()] for line in lines]
    total = 0

    for i in range(len(ans)):
        if test2(ans[i], nums[i]):
            total += ans[i]

    return total


example = io.StringIO("""
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip())
answer_1 = ""
answer_2 = "11387"

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
