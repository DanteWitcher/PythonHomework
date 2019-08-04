#!/usr/bin/env python
import argparse

from .classes.Launcher import Launcher
from .classes.Parser import Parser

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
    parser = Parser(args.__getattribute__(key))
    parser.parse()
    try:
        Launcher(parser.get_str()).run(parser.get_type())
    except (SyntaxError, NameError, TypeError) as e:
        # TO DO: implement normal ErrorHandler
        print('ERROR: ', e.__str__())


if __name__ == '__main__':
    main()
