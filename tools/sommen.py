"""
Small utility script for printing a bunch of calculations for my kids.
"""
import random
import sys
import webbrowser

NUMBER_OF_LINES = 100
if "floris" in sys.argv:
    PLUS_MAX = 10
    MINUS_MAX = 5
    TIMES_MAX = 5
else:
    PLUS_MAX = 300
    MINUS_MAX = 80
    TIMES_MAX = 24


def plus():
    a = random.choice(range(PLUS_MAX)) + 1
    b = random.choice(range(PLUS_MAX)) + 1
    return "%03s + %03s =" % (a, b)


def minus():
    a = random.choice(range(MINUS_MAX)) + 1
    b = random.choice(range(MINUS_MAX)) + 1
    total = a + b
    return "%03s - %03s =" % (total, b)


def times():
    a = random.choice(range(TIMES_MAX)) + 2
    b = random.choice(range(TIMES_MAX)) + 2
    return "%03s x %03s =" % (a, b)


def main():
    outfile = open("/tmp/sommen.txt", "w")
    if "floris" in sys.argv:
        actions = [plus, minus, times]
    else:
        actions = [plus, minus, times]
    for i in range(NUMBER_OF_LINES):
        line = "{}                          {}\n\n".format(
            random.choice(actions)(),
            random.choice(actions)(),
        )
        outfile.write(line)
    outfile.close()
    webbrowser.open("file:///tmp/sommen.txt")
