# Advent of code 2023
# Day 9

# Parse file
file_path = 'input/9.txt'
with open(file_path, 'r') as f:
    data = f.read().strip().split('\n')
    data = [[int(n) for n in x.split()] for x in data]

# Solve Problem
def build_diffs(row):
    diffs = [row]
    while any(n != 0 for n in diffs[-1]):
        line = [diffs[-1][i+1] - diffs[-1][i] for i in range(len(diffs[-1])-1)]
        diffs.append(line)
    return diffs

def predict(diffs):
    next = 0
    for i in range(len(diffs)-1,-1,-1):
        next += diffs[i][-1]
    return next

def backwards(diffs):
    back = 0
    for i in range(len(diffs)-1,-1,-1):
        back = diffs[i][0] - back
    return back

oasis1 = sum(predict(build_diffs(row)) for row in data)
print(oasis1)

oasis2 = sum(backwards(build_diffs(row)) for row in data)
print(oasis2)
