#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    tot = 0
    for i, s in enumerate(argv):
        if i > 0:
            tot = tot + int(s, base=10)
    print("{:d}".format(tot))
