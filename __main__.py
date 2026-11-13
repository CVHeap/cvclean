#!/usr/bin/env python3
'''
CV Clean: Command Line Entry Point

Usage: python3 -m cvclean [-h]
'''
import argparse
import functools
import sys

# CV Heap
import cvclean


def main():
    '''
    Process a command.
    '''
    options = parse_options()
    options.outfile.write(
        cvclean.apply_filters(options.infile.read()))


def parse_options():
    '''
    Return command line arguments.
    '''
    parser = argparse.ArgumentParser(
        usage='cvclean [-h] -i <input> -o <output>',
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, width=100))
    parser.add_argument(
        '-i', '--input',
        dest='infile',
        action='store',
        metavar='path',
        type=open,
        help='List of directories to scan (default: stdin)',
        default=sys.stdin)
    parser.add_argument(
        '-o', '--output',
        dest='outfile',
        action='store',
        metavar='path',
        type=functools.partial(open, mode='w'),
        help='Output directory for output logs (default: stdout)',
        default=sys.stdout)
    return parser.parse_args()


if __name__ == '__main__':
    main()
