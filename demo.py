#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import time

import conf  # noqa
from decorators import timelog, proflog


@timelog
@proflog()
def doit():
    time.sleep(5)
    print('Done')


def main(dry_run=False):
    doit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Demo script")
    parser.add_argument('-d', '--dry_run', action='store_true',
                        help='don\'t execute any actions, just log them')
    options = parser.parse_args()
    main(dry_run=options.dry_run)
