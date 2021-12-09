from ..day import Day
from .bassin import Bassin


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

    def get_index_from_coord(self, x, y) -> int:
        return x + (self.width * y)

    def at_index(self, index) -> int:
        if index < 0 or index > len(self.map) - 1:
            return 10

        return int(self.map[index])

    def at(self, x, y) -> int:
        index = self.get_index_from_coord(x, y)
        return self.at_index(index)

    def get_coord_from_index(self, index):
        x = index % self.width
        y = int(index / self.width)
        return x, y

    def get_neighboors_coords(self, x, y):
        return [
            (x + 1, y),  # Right
            (x - 1, y),  # Left
            (x, y + 1),  # Bottom
            (x, y - 1),  # Top
        ]

    def get_neighboors(self, x, y):

        neighboors = []
        for coord in self.get_neighboors_coords(x, y):
            neighboors.append(self.at(*coord))
        return neighboors

    def get_neighboors_indexes(self, index):
        x, y = self.get_coord_from_index(index)

        coords = self.get_neighboors_coords(x, y)

        def inRange(coord):
            xx, yy = coord
            return xx >= 0 and yy >= 0 and xx < self.width and yy < self.height

        coords = list(filter(inRange, coords))

        return [self.get_index_from_coord(*c) for c in coords]

    def draw(self):
        from .drawing import Drawing

        d = Drawing(self)

        d.start()

    def part1(self):

        # Easter egg
        # return self.draw()

        lows = []

        for index in range(len(self.map)):
            x, y = self.get_coord_from_index(index)
            pt = self.at(x, y)
            neighboors = self.get_neighboors(x, y)

            if all(pt < n for n in neighboors):
                lows.append(1 + pt)

        return sum(lows) + 2

    def part2(self):
        bassins = []
        for index in range(len(self.map)):
            x, y = self.get_coord_from_index(index)
            pt = self.at(x, y)
            neighboors = self.get_neighboors(x, y)

            if all(pt < n for n in neighboors):
                # start recursion
                bassin = Bassin(self, start=index)
                bassins.append(bassin)

        sorted_bassins = sorted(bassins, key=lambda x: len(x.pixels), reverse=True)
        sizes = [len(b.pixels) for b in sorted_bassins[:3]]

        return sizes[0] * sizes[1] * sizes[2]
