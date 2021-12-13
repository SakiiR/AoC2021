import enum
from ..day import Day


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @classmethod
    def fromLine(cls, line):
        x, y = [int(x) for x in line.split(",")]
        return cls(x, y)

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"


class FoldDirection(enum.Enum):
    VERTICAL = "x"
    HORIZONTAL = "y"


class Cell(enum.Enum):
    FILLED = "#"
    EMPTY = "."


class Fold:
    def __init__(self, direction, value) -> None:
        self.direction = direction
        self.value = value

    @classmethod
    def fromLine(cls, line):
        direction, value = line.split(" ")[-1].split("=")
        value = int(value)

        direction = FoldDirection(direction)

        return cls(direction, value)

    def __repr__(self) -> str:
        return f"Fold(direction={self.direction}, value={self.value})"


class Day13(Day):
    name = "Day 13"
    description = "Transparent Origami"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

        self.lines = self.input_file_content.splitlines()

        self.__points = []
        self.__folds = []

        self.__parse()

        self.width, self.height = self.__determine_size()

        self.__grid = [Cell.EMPTY for _ in range(self.width * self.height)]

        for point in self.__points:
            index = self.get_index_from_coord(point.x, point.y)
            self.__grid[index] = Cell.FILLED

    def fold(self, fold):
        if fold.direction == FoldDirection.HORIZONTAL:
            return self.fold_y(fold.value)
        if fold.direction == FoldDirection.VERTICAL:
            return self.fold_x(fold.value)

    def count_visible(self):
        s = 0
        for c in self.__grid:
            if c == Cell.FILLED:
                s += 1
        return s

    def fold_x(self, value):
        for x in range(value, self.width):
            for y in range(self.height):
                if self.at(x, y) == Cell.FILLED:
                    delta = x - value
                    # Empty the old value
                    self.write(x, y, Cell.EMPTY)
                    # Write the new value
                    self.write((value - delta), y, Cell.FILLED)

    def fold_y(self, value):
        for y in range(value, self.height):
            for x in range(self.width):
                if self.at(x, y) == Cell.FILLED:
                    delta = y - value
                    # Empty the old value
                    self.write(x, y, Cell.EMPTY)
                    # Write the new value
                    self.write(x, (value - delta), Cell.FILLED)

    def get_coord_from_index(self, index):
        x = index % self.width
        y = int(index / self.width)
        return x, y

    def get_index_from_coord(self, x, y) -> int:
        return x + (self.width * y)

    def write(self, x, y, value: Cell):
        self.__grid[self.get_index_from_coord(x, y)] = value
        return value

    def at(self, x, y) -> Cell:
        return self.__grid[self.get_index_from_coord(x, y)]

    def __parse(self):
        for line in self.lines:
            if "," in line:
                self.__points.append(Point.fromLine(line))
            if "fold" in line:
                self.__folds.append(Fold.fromLine(line))

    def __determine_size(self):
        maxx = 0
        maxy = 0

        for pt in self.__points:
            if pt.x > maxx:
                maxx = pt.x
            if pt.y > maxy:
                maxy = pt.y

        return maxx + 1, maxy + 1

    def __repr__(self) -> str:
        out = ""

        for y in range(self.height):
            out += f"{y:04d}. "
            for x in range(self.width):
                px = self.at(x, y)
                out += px.value
            out += "\n"
        return out.rstrip("\n")

    def part1(self):
        self.fold(self.__folds[0])
        return self.count_visible()

    def part2(self):
        return 0
