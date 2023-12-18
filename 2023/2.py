# Advent of code 2023
# Day 2
import re

ex = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

# Answer: 8
#
reference = {'red': 12, 'green': 13, 'blue': 14}


def possible(subset, reference):
    for category in subset:
        if category not in reference or subset[category] > reference[category]:
            return False
    return True


def parse_games(data):
    games = {}
    for line in data:
        game_number = re.findall(r"Game (\d+):", line)[0]
        segments = line.split(';')

        game_info = {}

        for i, segment in enumerate(segments, start=1):
            colors_counts = re.findall(r"(\d+) (\w+)", segment)
            game_info[f"Segment {i}"] = {color: int(count) for count, color in colors_counts}

        games[game_number] = game_info
    return games


def find_power(segments):
    power_dict = {}
    for segment in segments:
        for color, value in segment.items():
            if color not in power_dict:
                power_dict[color] = value
            power_dict[color] = max(power_dict[color], value)

    # Find Power
    product = 1
    for value in power_dict.values():
        product *= value
    return product


with open("input/2.txt") as file:
    games_dict = parse_games(file)
    # print(games_dict)

games_sum = 0
games_power = 0
for game in games_dict:
    game_info = games_dict[game]
    all_segments_possible = True

    for segment in game_info:
        if not possible(game_info[segment], reference):
            all_segments_possible = False
            break

    if all_segments_possible:
        games_sum += int(game)
        # print(game)

    power = find_power(game_info.values())
    print(f"Game {game} power: {power}")

    games_power += power

print("Total sum:", games_sum)
print("Total power:", games_power)
