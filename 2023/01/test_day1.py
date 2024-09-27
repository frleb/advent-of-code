import unittest

from day1 import find_calibration_value_p1, find_calibration_value_p2, part1, part2

from math import prod


class Day1Test(unittest.TestCase):

    def test_find_calibration_value_p1(self):
        self.assertEqual(find_calibration_value_p1("1abc2"), 12)
        self.assertEqual(find_calibration_value_p1("pqr3stu8vwx"), 38)
        self.assertEqual(find_calibration_value_p1("a1b2c3d4e5f"), 15)
        self.assertEqual(find_calibration_value_p1("treb7uchet"), 77)

    def test_part1(self):
        part1_data = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
        ]
        result = part1(part1_data)
        self.assertEqual(result, 142)

    def test_find_calibration_value_p2(self):
        self.assertEqual(find_calibration_value_p2("two1nine"), 29)
        self.assertEqual(find_calibration_value_p2("eightwothree"), 83)
        self.assertEqual(find_calibration_value_p2("abcone2threexyz"), 13)
        self.assertEqual(find_calibration_value_p2("xtwone3four"), 24)
        self.assertEqual(find_calibration_value_p2("4nineeightseven2"), 42)
        self.assertEqual(find_calibration_value_p2("zoneight234"), 14)
        self.assertEqual(find_calibration_value_p2("7pqrstsixteen"), 76)

    def test_part2(self):
        part2_data = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]

        self.assertEqual(part2(part2_data), 281)


if __name__ == "__main__":
    unittest.main()
