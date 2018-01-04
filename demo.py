#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import time

import conf  # noqa
from decorators import timelog


@timelog
def doit(n=None):
    """Returns the n argument or prints Done.

    >>> [doit(5) for n in range(3)]
    [5, 5, 5]"""
    time.sleep(1)
    if n is None:
        print('Done')
    return n


def main(dry_run=False):
    doit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Demo script")
    parser.add_argument('-d', '--dry_run', action='store_true',
                        help='don\'t execute any actions, just log them')
    options = parser.parse_args()
    main(dry_run=options.dry_run)
