# Advent of code 2024
# Day 09
import io


def p1(f):
    line = f.read().strip()
    expanded = []
    block = 0

    #Expand
    for i in range(len(line)):
        if i % 2 == 0:
            expanded += [block] * int(line[i])
            block += 1
        else:
            expanded += '.' * int(line[i])

    #Collapse
    for i in range(len(expanded)):
        while expanded[-1] == '.':
            expanded.pop()
        if i < len(expanded) and expanded[i] == '.':
            expanded[i] = expanded.pop()

    return sum((i * int(char)) for i, char in enumerate(expanded) if char != '.')


def p2(f): # Approach from HN
    line = f.read().strip()
    files = {}
    free = []
    block = 0
    pos = 0

    # Expand
    for i in range(len(line)):
        c = int(line[i])
        if i % 2 == 0:
            files[block] = (pos, c)
            block += 1
        else:
            free.append((pos, c))
        pos += c

    # For each block going backwards, try to switch to empty space going forwards
    while block > 0:
        block -= 1
        pos, size = files[block]
        for i, (start, length) in enumerate(free):
            if start >= pos:
                free = free[:i]
                break
            if size <= length:
                files[block] = (start, size)
                if size == length:
                    free.pop(i)
                else:
                    free[i] = (start + size, length - size)
                break

    return sum(block * i for block, (pos, size) in files.items() for i in range(pos, pos+size))


example = io.StringIO("""
2333133121414131402
""".strip())
answer_1 = ""
answer_2 = "2858"

# For debugging purposes
def main():
    print(p1(example))
    example.seek(0)
    print(p2(example))

if __name__ == '__main__':
    main()
