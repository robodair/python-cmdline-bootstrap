# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.2.0"


import sys
import argparse


def main():
    """
    Run the program
    """

    print "Executing bootstrap version %s." % __version__
    print "List of argument strings: %s" % sys.argv[1:]

    parser = argparse.ArgumentParser(prog='bootstrap')
    parser.add_argument('--dry-run', action='store_true', help='Dry Run - make no actual changes')
    subparsers = parser.add_subparsers(help='Allowed subcommands')


    # create the parser for the "submit" command
    parser_a = subparsers.add_parser('submit', help='submit your changes')
    parser_a.add_argument('file', help='the file to submit')
    parser_a.set_defaults(func=submit)

    # create the parser for the "status" command
    parser_b = subparsers.add_parser('status', help='view the status')
    parser_b.add_argument('directory', help='the directory to status')
    parser_b.add_argument('--opt', choices=['XYZ', '123'], help='choose between XYZ options')
    parser_b.set_defaults(func=status)

    args = parser.parse_args()
    args.func(args)

def submit(args):
    print 'called submit'
    print args

def status(args):
    print 'called status'
    print args
