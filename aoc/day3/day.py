from typing import List
from ..day import Day


def get_most_common_bits(lst: List[int]):
    ones = len(list(filter(lambda x: x == 1, lst)))
    zeros = len(list(filter(lambda x: x == 0, lst)))
    if ones > zeros:
        return 1
    return 0


def get_least_common_bits(lst: List[int]):
    ones = len(list(filter(lambda x: x == 1, lst)))
    zeros = len(list(filter(lambda x: x == 0, lst)))
    if ones > zeros:
        return 0
    return 1


def get_epsilon_bit(lst: List):
    return get_least_common_bits(lst)


def get_gamma_bit(lst: List):
    return get_most_common_bits(lst)


def select_bit(n: int, index: int):
    if (n & (1 << index)) != 0:
        return 1
    return 0


def bit_repr(n: int, bits=8):
    return bin(n).replace("0b", "").rjust(bits, "0")


class Day3(Day):
    name = "Day 3"
    description = "Binary Diagnostic"

    def __init__(self, test=False) -> None:
        self.getPaths(__file__)
        super().__init__(test)

        ## Init vars
        self.lines = self.input_file_content.splitlines()
        self.bit_count = len(self.lines[0])
        self.numbers = [int(x, 2) for x in self.lines]

    def go(self):
        gamma_bits = []
        epsilon_bits = []
        for bit_index in range(self.bit_count)[::-1]:
            bits = []
            for n in self.numbers:
                bit = select_bit(n, bit_index)
                bits.append(bit)
            gamma_bits.append(get_gamma_bit(bits))
            epsilon_bits.append(get_epsilon_bit(bits))

        gamma = int("".join([str(x) for x in gamma_bits]), 2)
        epsilon = int("".join([str(x) for x in epsilon_bits]), 2)
        power_consumption = gamma * epsilon
        return power_consumption

    def part1(self):
        return self.go()

    def part2(self):
        return 0
