# Advent of code 2023
# Day 1
import re

ex1 = "1abc2"
ex2 = "pqr3stu8vwx"
ex3 = "a1b2c3d4e5f"
ex4 = "treb7uchet"
ex = [ex1, ex2, ex3, ex4]

# records = [ex1, ex2, ex3, ex4]
records = []
with open("input/1.txt") as file:
    for line in file:  # Line in Ex to test example
        digits = re.findall(r'\d', line)
        fl = digits[0] + digits[-1]
        records.append(int(fl))
        # print(fl)
print(sum(records))

# Part 2

ex5 = "two1nine"
ex6 = "eightwothree"
ex7 = "abcone2threexyz"
ex8 = "xtwone3four"
ex9 = "4nineeightseven2"
ex10 = "zoneight234"
ex11 = "7pqrstsixteen"
exs = [ex5, ex6, ex7, ex8, ex9, ex10, ex11]

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
# Adding these together produces 281.

words_to_int = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}  # , 'zero': 0}
pattern = '|'.join(words_to_int.keys()) + r'|\d'


records = []
with open("input/1.txt") as file:
    for line in file:
        # New way handles overlapping matches
        digits = []
        for i in range(len(line)):
            match = re.search(pattern, line[i:])
            if match:
                digits.append(match.group())

        # digits = re.findall(pattern, line)
        # print(digits)

        digits = [str( words_to_int.get(digit) ) if digit in words_to_int else (digit) for digit in digits]

        fl = digits[0] + digits[-1]
        records.append(int(fl))
        # print(fl)
print(sum(records))
