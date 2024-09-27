import pathlib
import re


def parse_data():
    path = "input.txt"
    return pathlib.Path(path).read_text().rstrip().splitlines()


def word_to_digit(word: str) -> int:
    match word:
        case "one" | "1":
            return "1"
        case "two" | "2":
            return "2"
        case "three" | "3":
            return "3"
        case "four" | "4":
            return "4"
        case "five" | "5":
            return "5"
        case "six" | "6":
            return "6"
        case "seven" | "7":
            return "7"
        case "eight" | "8":
            return "8"
        case "nine" | "9":
            return "9"


def find_calibration_value_p1(line: str) -> int:
    digits = [char for char in line if char.isdigit()]
    return int(digits[0] + digits[-1])


def find_calibration_value_p2(line: str) -> int:
    digits = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)

    return int(word_to_digit(digits[0]) + word_to_digit(digits[-1]))


def part1(input) -> int:
    return sum(find_calibration_value_p1(line=line) for line in input)


def part2(input) -> int:
    return sum(find_calibration_value_p2(line=line) for line in input)


if __name__ == "__main__":
    input = parse_data()

    print(part1(input))
    # part1 : 54388

    print(part2(input))
    # part2 : 53515
