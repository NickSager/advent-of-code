# Advent of code 2023
# Day 7

import fileinput
from collections import Counter

hands = []

# Parse file
file_path = 'input/7ex.txt'
with open(file_path, 'r') as f:
    for line in f:
        hand, bid = line.split()
        hands.append((hand, int(bid)))

# Fileinput method. cat file | python 7.py
# for line in fileinput.input():
#     hand, bid = line.split()
#     hands.append((hand, int(bid)))


# Solve Problem
def score(hand, part2=False):
    if part2 and hand != 'JJJJJ':
        hand = hand.replace('J', Counter(c for c in hand if c != 'J').most_common(1)[0][0])
    hand = Counter(hand).most_common()


    if hand[0][1] == 5:
        return 1
    elif hand[0][1] == 4:
        return 2
    elif hand[0][1]==3:
        if hand[1][1]==2:
            return 3  # Full House
        else:
            return 4  # Three of a kind
    elif hand[0][1] == 2:
        if hand[1][1] == 2:
            return 5  # Two pair
        else:
            return 6 # One pair
    else:
        return 7  # High Card

def sort_hands(hands, rank, part2=False):
    sorted_hands = sorted(
        hands,
        key = lambda h: (  # Help from GPT-4 on this ranking section
            score(h[0], part2),
            tuple(rank.index(card) for card in h[0])
        ), reverse = True
    )
    return sorted_hands


rank_1 = "AKQJT98765432"
pt_1 = 0

for i, (hand, bid) in enumerate(sort_hands(hands, rank_1), start = 1):
    pt_1 += i * bid

print("Part 1:", pt_1)

# Part 2
rank_2 = "AKQT98765432J"
pt_2 = 0

for i, (hand, bid) in enumerate(sort_hands(hands, rank_2, True), start = 1):
    pt_2 += i * bid

print("Part 2:", pt_2)
