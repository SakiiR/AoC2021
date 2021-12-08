import enum
from ..day import Day


class Action(enum.Enum):
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"


class Submarine:
    def __init__(self) -> None:
        self.depth = 0
        self.horizontal = 0

    def process(self, instruction: dict):
        action: Action = instruction.get("action")
        count: int = instruction.get("count")

        if action == action.FORWARD:
            self.horizontal += count
        if action == action.DOWN:
            self.depth += count
        if action == action.UP:
            self.depth -= count

    def compute(self):
        return self.horizontal * self.depth


class AdvancedSubmarine:
    def __init__(self) -> None:
        self.depth = 0
        self.horizontal = 0
        self.aim = 0

    def process(self, instruction: dict):
        action: Action = instruction.get("action")
        count: int = instruction.get("count")

        if action == action.FORWARD:
            self.horizontal += count
            self.depth += self.aim * count
        if action == action.DOWN:
            self.aim += count
        if action == action.UP:
            self.aim -= count

    def compute(self):
        return self.horizontal * self.depth


class Day2(Day):
    name = "Day 2"
    description = "Dive!"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

        self.instructions = [
            {"action": Action(a), "count": int(b)}
            for a, b in [x.split(" ") for x in self.input_file_content.splitlines()]
        ]

    def part1(self):
        s = Submarine()

        for ins in self.instructions:
            s.process(ins)
        return s.compute()

    def part2(self):
        s = AdvancedSubmarine()

        for ins in self.instructions:
            s.process(ins)
        return s.compute()
