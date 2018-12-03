import csv
from collections import namedtuple
import logging


logger = logging.getLogger(__name__)

DataPoint = namedtuple('DataPoint', ['strain', 'force'])

def load_tra(filename: str, sep=';') -> list:
    """
    Loading the TRA into a list of namedtuples.
    tra_data = load_tra(tra_filename)
    data_point = tra_data[42]
    data_point.strain  # strain value as float e.g.: 0.3
    data_point.force  # force value as float e.g.: 13.9
    """

    data = []
    with open(filename, 'r') as f:
        logger.info('Reading %s' % filename)
        reader = csv.reader(f, delimiter=';')
        header = next(reader)  # throwing away header
        logger.debug('Throwing away header: %s' % header)
        for datarow in reader:
            strain = float(datarow[0].strip().replace(',', '.'))
            force = float(datarow[1].strip().replace(',', '.'))
            datapoint = DataPoint(strain, force)
            data.append(datapoint)
    return data


if __name__ == '__main__':
    data = load_tra('test_data.tra')
    print(data)