import sys

FLAG = "flag{y0u_l34k3d_m3!}"
PUBLIC_DATA = "RainRainGoAwayComeAgainAnotherDay"


def main():
    haystack = FLAG + PUBLIC_DATA
    write("Welcome to the Infoleak!\n")
    write("Please enter an index: ")

    index = len(FLAG) + int(sys.stdin.readline())
    write("Giving you the data from index %d...\n" % index)
    write("Here's the data: %s\n" % haystack[index:])


def write(data):
    sys.stdout.write(data)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
