#!/usr/bin/env python

import sys

# I could be clever, or I could just use a big lookup table
encoding = {"10-001": "1",
            "01-001": "2",
            "11-000": "3",
            "00-101": "4",
            "10-100": "5",
            "01-100": "6",
            "00-011": "7",
            "10-010": "8",
            "01-010": "9",
            "00-110": "0",
            "100-01": "A",
            "010-01": "B",
            "110-00": "C",
            "001-01": "D",
            "101-00": "E",
            "011-00": "F",
            "000-11": "G",
            "100-10": "H",
            "010-10": "I",
            "001-10": "J",
            "1000-1": "K",
            "0100-1": "L",
            "1100-0": "M",
            "0010-1": "N",
            "1010-0": "O",
            "0110-0": "P",
            "0001-1": "Q",
            "1001-0": "R",
            "0101-0": "S",
            "0011-0": "T",
            "1-0001": "U",
            "0-1001": "V",
            "1-1000": "W",
            "0-0101": "X",
            "1-0100": "Y",
            "0-1100": "Z",
            "0-0011": "-",
            "1-0010": ".",
            "0-1010": " ",
            "0-0110": "*",
            "0-0-0-00": "$",
            "0-0-00-0": "/",
            "0-00-0-0": "+",
            "00-0-0-0": "%"}


def decode(s):
    decoded = []
    index = 0
    while True:
        c = s[index:index+6]
        if c.count('-') > 1:
            print("extended characters not supported, lol")
            print("so far we had: %s" % ''.join(decoded))
            sys.exit()
        try:
            decoded.append(encoding[c])
        except:
            print("decoding error: whoops")
            print("so far we had: %s" % ''.join(decoded))
            sys.exit()
        index += 6
        if index == len(s):
            break
        if index > len(s):
            print("decoding error: bad number of digits")
            print("so far we had: %s" % ''.join(decoded))
            sys.exit()
    print("%s" % ''.join(decoded))


if __name__ == '__main__':
    decode(sys.argv[1])
