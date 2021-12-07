#!/usr/bin/env python
# @SakiiR

import sys
from ..day import Day


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def cpy(self):
        return self.__class__(self.x, self.y)

    def __str__(self) -> str:
        return f"Point({self.x:06d}, {self.y:06d})"

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y


class Vector:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @classmethod
    def from_line(cls, line):
        tokens = line.split(" -> ")

        x1, y1 = [int(x) for x in tokens[0].split(",")]
        x2, y2 = [int(x) for x in tokens[1].split(",")]

        return cls(x1, y1, x2, y2)

    def get_points(self, diagonals: bool):
        points = []

        if self.x1 == self.x2:
            if self.y1 < self.y2:
                for y in range(self.y1, self.y2 + 1):
                    points.append(Point(self.x1, y))
            if self.y1 > self.y2:
                for y in range(self.y2, self.y1 + 1):
                    points.append(Point(self.x1, y))
            return points

        if self.y1 == self.y2:
            if self.x1 < self.x2:
                for x in range(self.x1, self.x2 + 1):
                    points.append(Point(x, self.y1))
            if self.x1 > self.x2:
                for x in range(self.x2, self.x1 + 1):
                    points.append(Point(x, self.y1))
            return points

        # Diagonals :/
        if diagonals:
            it = Point(self.x1, self.y1)
            dest = Point(self.x2, self.y2)
            points.append(it.cpy())

            while it != dest:
                it.x += 1 if it.x < dest.x else -1
                it.y += 1 if it.y < dest.y else -1
                points.append(it.cpy())

        return points

    def __str__(self) -> str:
        return f"Vector({self.x1:06d},{self.y1:06d} -> {self.x2:06d}, {self.y2:06d})"


class Board:
    def __init__(self, file_content, diagonals=False) -> None:
        self.__file_content = file_content
        self.__vectors = []
        self.__board = []
        self.width = 0
        self.height = 0
        self.__diagonals = diagonals

    def __determine_size(self):
        maxx = 0
        maxy = 0

        for vector in self.__vectors:
            if vector.x1 > maxx:
                maxx = vector.x1
            if vector.x2 > maxx:
                maxx = vector.x2
            if vector.y1 > maxy:
                maxy = vector.y1
            if vector.y2 > maxy:
                maxy = vector.y2

        return maxx + 1, maxy + 1

    def __write_point(self, p: Point):
        self.__board[p.y][p.x] += 1

    def __draw(self):
        for vector in self.__vectors:
            # print(f"Drawing: {vector}")
            points = vector.get_points(self.__diagonals)
            for point in points:
                # print(f"Drawing: {point}")
                self.__write_point(point)

    def compute(self):
        s = 0
        for y in self.__board:
            for value in y:
                if value >= 2:
                    s += 1
        return s

    def parse(self):
        lines = self.__file_content.splitlines()
        for line in lines:
            self.__vectors.append(Vector.from_line(line))

        self.width, self.height = self.__determine_size()

        self.__board = [[0 for _ in range(self.width)] for _ in range(self.height)]

        self.__draw()

    def __str__(self) -> str:
        out = ""
        for y in self.__board:
            for x in y:
                if x == 0:
                    out += "."
                else:
                    out += str(x)
            out += "\n"
        return out


class Day5(Day):
    name = "Day 5"
    description = "Hydrothermal Venture"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

    def part1(self):
        b = Board(self.input_file_content)
        b.parse()
        return b.compute()

    def part2(self):
        b = Board(self.input_file_content, diagonals=True)
        b.parse()
        return b.compute()
