from ..day import Day


class Day9(Day):
    name = "Day 9"
    description = "Smoke Basin"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

        self.lines = self.input_file_content.splitlines()

        self.width = len(self.lines[0])
        self.height = len(self.lines)

        self.map = ""
        for line in self.lines:
            self.map += line

    def at(self, x, y) -> int:
        index = x + (self.width * y)

        if index < 0 or index > len(self.map) - 1:
            return 10

        return int(self.map[index])

    def get_coord_from_index(self, index):
        x = index % self.width
        y = int(index / self.width)
        return x, y

    def neighboors(self, x, y):
        return [
            self.at(x + 1, y),  # Right
            self.at(x - 1, y),  # Left
            self.at(x, y + 1),  # Bottom
            self.at(x, y - 1),  # Top
            # self.at(x + 1, y + 1),  # Bottom Right
            # self.at(x - 1, y - 1),  # Top Left
            # self.at(x - 1, y + 1),  # Bottom Left
            # self.at(x + 1, y - 1),  # Top Right
        ]

    def part1(self):
        lows = []

        for index in range(len(self.map)):
            x, y = self.get_coord_from_index(index)
            pt = self.at(x, y)
            neighboors = self.neighboors(x, y)

            if all(pt < n for n in neighboors):
                lows.append(1 + pt)

        return sum(lows)

    def part2(self):
        return 0
