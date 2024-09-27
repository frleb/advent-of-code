import pathlib
import re


def parse_data():
    path = "input.txt"
    return pathlib.Path(path).read_text().rstrip().splitlines()


def is_bag_valid(bag: dict) -> bool:
    MAX_BLUE_CUBES = 14
    MAX_GREEN_CUBES = 13
    MAX_RED_CUBES = 12

    if (
        bag["blue"] > MAX_BLUE_CUBES
        or bag["green"] > MAX_GREEN_CUBES
        or bag["red"] > MAX_RED_CUBES
    ):
        return False

    return True


def parse_game(line):
    game_input, rounds_input = line.split(": ")
    game_id = int(game_input.split(" ")[1])
    PULLED_CUBES_PATTERN = r"(\d+) (blue|green|red)+"
    pulled_cubes = re.findall(pattern=PULLED_CUBES_PATTERN, string=rounds_input)

    return game_id, pulled_cubes


def part1(input) -> int:
    sum_of_possible_games = 0

    for line in input:
        bag = {"blue": 0, "green": 0, "red": 0}

        game_id, rounds = parse_game(line)

        for round in rounds:
            bag[round[1]] = max(bag[round[1]], int(round[0]))

        if is_bag_valid(bag):
            sum_of_possible_games += game_id

    return sum_of_possible_games


def part2(input) -> int:
    sum_of_possible_games = 0

    for line in input:
        bag = {"blue": 0, "green": 0, "red": 0}

        game_id, rounds = parse_game(line)

        for round in rounds:
            bag[round[1]] = max(bag[round[1]], int(round[0]))

        sum_of_possible_games += bag["blue"] * bag["green"] * bag["red"]

    return sum_of_possible_games


if __name__ == "__main__":
    input = parse_data()

    print(part1(input))
    assert part1(input) == 2207

    print(part2(input))
    assert part2(input) == 62241
