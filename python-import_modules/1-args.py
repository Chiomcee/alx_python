#!/usr/bin/python3

import sys


if __name__ == "__main__":
    args = sys.argv[1:]   # Exclude the script name from the arguments
    # Determine the number of arguments
    num_args = len(args)

    # print the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))
    # print the arguments
    for i, arg in enumerate(args):
        print("{}: {}".format(i + 1, arg))
