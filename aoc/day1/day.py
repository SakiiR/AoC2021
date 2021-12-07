from os import path
from ..day import Day


def go(numbers):
    prev = None
    count = 0
    for n in numbers:
        if prev:
            if n > prev:
                count += 1
        prev = n
    return count


class Day1(Day):
    name = "Day 1"
    description = "Sonar Sweep"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

    def part1(self):
        lines = [int(x) for x in self.input_file_content.splitlines()]
        return go(lines)

    def part2(self):
        lines = [int(x) for x in self.input_file_content.splitlines()]
        return go(lines)
