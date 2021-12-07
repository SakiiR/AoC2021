#!/usr/bin/env python
# @SakiiR


from typing import List
import sys

from ..day import Day


class Board:
    def __init__(self, data: List[List]) -> None:
        self.__data = data
        self.__marked_numbers = []
        self.__won = False

    def mark(self, number):
        if self.__won:
            return
        self.__marked_numbers.append(number)

    def reset(self):
        self.__marked_numbers = []
        self.__won = False

    def won(self):

        if self.__won:
            return True

        # Check rows
        def check(arr, marked_numbers):
            for line in arr:
                result = all(x in marked_numbers for x in line)
                if result:
                    return True
            return False

        if check(self.__data, self.__marked_numbers):
            self.__won = True
            return True

        # Check columns
        size = len(self.__data[0])
        columns = []
        for i in range(size):
            column = []
            for j in range(size):
                column.append(self.__data[j][i])
            columns.append(column)

        if check(columns, self.__marked_numbers):
            self.__won = True
            return True

        return False

    def compute(self):
        s = 0
        for line in self.__data:
            for x in line:
                if x not in self.__marked_numbers:
                    s += x

        n = self.__marked_numbers[-1]

        return n * s

    def __str__(self) -> str:
        out = ""
        for line in self.__data:
            for number in line:
                if number in self.__marked_numbers:
                    out += "  X "
                else:
                    out += f"{number: 3d} "
            out += "\n"
        return out


class Bingo:
    def __init__(self, input_data: str) -> None:
        self.__input = input_data.splitlines()

    def pop_line(self):
        try:
            return self.__input.pop(0)
        except IndexError:
            return

    def parse(self):
        self.__random_numbers = [int(x) for x in self.pop_line().split(",")]
        self.__boards = []
        while True:
            lines = []
            self.pop_line()

            def parse_line(line):
                return [int(x) for x in list(filter(None, line.split(" ")))]

            for _ in range(5):
                line = self.pop_line()
                if not line:
                    return
                nbs = parse_line(line)
                lines.append([int(x) for x in nbs])

            self.__boards.append(Board(lines))

    def part1(self):
        for n in self.__random_numbers:
            for board in self.__boards:
                board.mark(n)
                if board.won():
                    solution = board.compute()
                    return solution

    def part2(self):
        winning = []
        board_count = len(self.__boards)
        for n in self.__random_numbers:
            for board in self.__boards:
                board.mark(n)
                if board.won() and board not in winning:
                    winning.append(board)
                    if len(winning) == board_count - 1:
                        last_winning_board = list(
                            filter(lambda x: x not in winning, self.__boards)
                        )[0]
                        last_winning_board.reset()

                        for n in self.__random_numbers:
                            last_winning_board.mark(n)
                            if last_winning_board.won():
                                solution = last_winning_board.compute()
                                return solution


class Day4(Day):
    name = "Day 4"
    description = "Giant Squid"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

    def part1(self):
        b = Bingo(self.input_file_content)
        b.parse()
        return b.part1()

    def part2(self):
        b = Bingo(self.input_file_content)
        b.parse()
        return b.part2()
