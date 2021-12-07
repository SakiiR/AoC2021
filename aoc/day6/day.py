from typing import List
from ..day import Day


def go(data: List[int], n=256):
    fishes = [0 for _ in range(9)]
    for fish in data:
        fishes[fish] += 1
    for _ in range(n):
        fishes.append(fishes.pop(0))
        fishes[6] += fishes[8]
    return sum(fishes)


class Day6(Day):
    name = "Day 6"
    description = "Lanternfish"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

        self.__state = [int(x) for x in self.input_file_content.split(",")]

    def part1(self):
        return go(self.__state, n=80)

    def part2(self):
        return go(self.__state, n=256)
