#!/usr/bin/env python
import argparse

from calculator.classes.Launcher import Launcher

# name of cli
key = 'pycalc'


def main():
    my_parser = argparse.ArgumentParser(description="Pure-python command-line calculator.")

    # Add the arguments
    my_parser.add_argument(key,
                           metavar='EXPRESSION',
                           type=str,
                           help='expression	string to evaluate')

    # Execute the parse_args() method
    args = my_parser.parse_args()
    # Launch
    args.__getattribute__(key)
    Launcher(args.__getattribute__(key)).run()
# 9


if __name__ == '__main__':
    main()
