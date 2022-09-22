#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leng = len(argv) - 1
    if leng == 0:
        print("{} arguments.".format(leng))
    elif leng == 1:
        print("{} argument:".format(leng))
    else:
        print("{} arguments:".format(leng))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
