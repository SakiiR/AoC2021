#!/usr/bin/env python
# @SakiiR

import sys


def inv(n):
    s = bin(n).replace("0b", "").replace("1", "2").replace("0", "1").replace("2", "0")
    return int(s, 2)


def go(numbers, maxbits):
    out = ""
    for bit in range(maxbits)[::-1]:
        bitaun = 0
        bitazero = 0
        for n in numbers:
            if (1 << bit) & n > 0:
                bitaun += 1
            else:
                bitazero += 1
        if bitaun > bitazero:
            out += "1"
        else:
            out += "0"

    gammarate = int(out, 2)


def process(filename):
    with open(filename, "rb") as fp:
        lines = fp.read().splitlines()
        maxbits = len(lines[0])
        numbers = [int(x, 2) for x in lines]
        go(numbers, maxbits)
        fp.close()


def main(argv):
    if len(argv) < 2:
        print(f"USAGE: {argv[0]} FILEPATH")
        return

    process(argv[1])


if __name__ == "__main__":
    main(sys.argv)
