#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    s = 0
    if len(argv) >= 2:
        for i in range(len(argv)):
            if i >= 1:
                s += int(argv[i])
    print("{}".format(s))
