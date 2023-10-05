#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(argv) == 2:
        print("{} {}".format(len(argv[1:]), "argument"), end="")
    else:
        print("{} {}".format(len(argv[1:]), "arguments"), end="")
    if len(argv) == 1:
        print("{}".format("."))
    else:
        print("{}".format(":"))
    if len(argv) >= 2:
        for i in range(len(argv)):
            if i >= 1:
                print("{}: {}".format(i, argv[i]))
