#!/usr/bin/python

import sys
import logging
import csv
import argparse
from collections import namedtuple
from bar_chart_creator import draw_chart


NAME_INDEX = 0
AVG_FORCE = 1
DEV_FORCE = 2
AVG_SIGMA = 3
DEV_SIGMA = 4

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__file__)

def create_chart(filename: str, title: str, y_name: str, header_length: int=1):
    # create datastructure to hold the data from csv
    logging.info('Creating datastructure to hold data')
    DataRow = namedtuple('Result', 'name,avg_f,dev_f,avg_s,dev_s')
    datarows = []

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            DRAW = len(row) - 1  # always the last column is the mark to draw
            if row[DRAW] and row[DRAW].lower() in 'yxio':
                _row = DataRow(row[NAME_INDEX],
                               row[AVG_FORCE],
                               row[DEV_FORCE],
                               row[AVG_SIGMA],
                               row[DEV_SIGMA])
                datarows.append(_row)
                logger.debug(f'Saving: {_row}')

    names = [row.name for row in datarows]
    avgs = [float(row.avg_s) for row in datarows]
    stdevs = [float(row.dev_s) for row in datarows]

    draw_chart(title=title, y_name=y_name, x_names=names,
               avgs=avgs, stdevs=stdevs)


def parse_args(args):
    parser = argparse.ArgumentParser(description='Get csv argument to draw pychart')
    parser.add_argument('-f', '--filename', type=str, action='store')
    parser.add_argument('-t', '--title', type=str, action='store')
    parser.add_argument('-n', '--y_name', type=str, action='store')
    return parser.parse_args(args=args)


if __name__ == '__main__':
    logger.info('Parsing args')
    args = parse_args(sys.argv[1:])
    filename = args.filename
    logger.info('Creating chart based on: %s' % filename)
    create_chart(filename=args.filename, title=args.title, y_name=args.y_name)
