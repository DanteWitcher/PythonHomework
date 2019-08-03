#!/usr/bin/env python
import argparse
from calculator.classes.Parser import Parser
from calculator.classes.Launcher import Launcher


# name of cli
key = 'pycalc'


def main():
    my_parser = argparse.ArgumentParser(description='Pure-python command-line calculator.')

    # Add the arguments
    my_parser.add_argument(key,
                           metavar='EXPRESSION',
                           type=str,
                           help='expression	string to evaluate')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    parser = Parser(args.__getattribute__(key))
    parser.parse()
    Launcher(parser.get_str()).run(parser.get_type())


if __name__ == '__main__':
    main()

