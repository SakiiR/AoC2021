from os import path
from ..day import Day


def part1(numbers):
    prev = None
    count = 0
    for n in numbers:
        if prev:
            if n > prev:
                count += 1
        prev = n
    return count


def part2(numbers):
    count = 0
    prev = None
    for i in range(len(numbers)):
        s = sum(numbers[i : i + 3])
        if prev:
            if s > prev:
                count += 1
        prev = s
    return count


class Day1(Day):
    name = "Day 1"
    description = "Sonar Sweep"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)
        self.lines = [int(x) for x in self.input_file_content.splitlines()]

    def part1(self):
        return part1(self.lines)

    def part2(self):
        return part2(self.lines)
