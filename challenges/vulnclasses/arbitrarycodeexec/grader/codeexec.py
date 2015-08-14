#! /usr/bin/python

import sys


def main():
    write("SuperCalculator (e.g. 2+2): ")
    eqn = sys.stdin.readline().strip()
    answer = eval(eqn)
    write("%s = %s\n" % (eqn, answer))


def write(data):
    sys.stdout.write(data)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
