from functools import cache
from typing import List
from ..day import Day


@cache
def compute_cost(distance):
    fuel = 0
    s = 0
    for _ in range(distance):
        fuel += 1 + s
        s += 1
    return fuel


def simulate2(state: List[int], pos: int):
    fuel = 0
    for e in state:
        fuel += compute_cost(abs(e - pos))
    return fuel


def simulate1(state: List[int], pos: int):
    fuel = 0
    for e in state:
        fuel += abs(e - pos)
    return fuel


class Day7(Day):
    name = "Day 7"
    description = "The Treachery of Whales"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

    def go(self, part2=False):
        state = [int(x) for x in self.input_file_content.split(",")]

        results = {}
        for target in range(min(state), max(state)):
            if part2:
                results[simulate2(state, target)] = target
            else:
                results[simulate1(state, target)] = target

        lowest_cons = min(results.keys())

        return lowest_cons

    def part1(self):
        return self.go()

    def part2(self):
        return self.go(part2=True)
