from aoc.day import Day
from aoc.day13.day13 import Day13
from aoc.day5.day import Day5
from .day1.day import Day1
from .day2.day import Day2
from .day3.day import Day3
from .day4.day import Day4
from .day5.day import Day5
from .day6.day import Day6
from .day7.day import Day7
from .day8.day import Day8
from .day9.day import Day9

import click

from time import perf_counter_ns as p


class NotCompleted(Day):
    name = "day"
    description = "not completed"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

    def part1(self):
        return 0

    def part2(self):
        return 0


@click.command()
@click.option("--last/--all", default=False)
@click.option("--test/--full", default=False)
@click.option("--day", type=click.INT, default=0)
def main(last, test, day):

    _ = NotCompleted(test=test)

    modules = [
        Day1(test=test),
        Day2(test=test),
        Day3(test=test),
        Day4(test=test),
        Day5(test=test),
        Day6(test=test),
        Day7(test=test),
        Day8(test=test),
        Day9(test=test),
        _,
        _,
        _,
        Day13(test=test),
    ]

    if day > 0:
        modules = [modules[day - 1]]

    if last:
        modules = [modules[-1]]

    for module in modules:
        part1_start_t = p()
        part1_s = module.part1()
        part1_stop_t = p()

        part2_start_t = p()
        part2_s = module.part2()
        part2_stop_t = p()

        print(f"# {module.name} - {module.description}:")
        if type(part1_s) == int:
            print(f"  1. `{part1_s:20d}` (ran in {part1_stop_t-part1_start_t:20d}ns)")
        else:
            print(f"  1. `{1337:20d}` (ran in {part1_stop_t-part1_start_t:20d}ns): ")
            print("```")
            print(part1_s)
            print("```")

        if type(part2_s) == int:
            print(f"  2. `{part2_s:20d}` (ran in {part2_stop_t-part2_start_t:20d}ns)")
        else:
            print(f"  2. `{1337:20d}` (ran in {part2_stop_t-part2_start_t:20d}ns): ")
            print("```")
            print(part2_s)
            print("```")
        print(f"")
