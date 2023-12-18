# Advent of code 2023
# Day 15
import io
from collections import defaultdict

def hash_str(s) -> int:
    hash = 0
    for c in s:
        hash += ord(c)
        hash *= 17
        hash = hash % 256

    return hash

def p1(f):
    input = f.read().strip().split(',')
    total = 0

    for str in input:
        total += hash_str(str)

    return total

def p2(f):
    input = f.read().strip().split(',')
    total = 0

    # hashmap = {i: {} for i in range(256)}
    hashmap = defaultdict(dict)
    for line in input:
        if '-' in line:
            label = line[:-1]
            box = hash_str(label)
            # hashmap[box][label] = None
            if label in hashmap[box]:
                hashmap[box].pop(label)

        elif '=' in line:
            label, length = line.split('=')
            box = hash_str(label)
            hashmap[box][label] = int(length)

        else:
            raise Exception("Invalid input")

    for i, box in hashmap.items():
        for j, length in enumerate(box.values()):
            total += (i+1) * (j+1) * length

    return total

example = io.StringIO("""
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""")

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
