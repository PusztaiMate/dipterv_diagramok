import os
import logging
from measure_statistics import Series


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__file__)

folder_name_map = {
    '10_20': '10/20',
    '20_10': '20/10',
    '10_125': '10m%,125μ',
    '25_125': '25m%,125μ',
    '40_125': '40m%,125μ',
    '10_250': '10m%,250μ',
    '25_250': '25m%,250μ',
    '40_250': '40m%,250μ',
    'eros_190': 'Erősített,190°C',
    'eros_215': 'Erősített,215°C',
    'eros_240': 'Erősített,240°C',
    # 'szines_190': 'Színezett,190°C',
    'szines_215': 'Színezett,215°C',
    'szines_240': 'Színezett,240°C',
    'szines_250bar': 'Színezett,250bar',
    'szines_650': 'Színezett,650bar',
    'szintelen_190': 'Áttetsző,190°C',
    'szintelen_215': 'Áttetsző,215°C',
    'szintelen_240': 'Áttetsző,240°C',
    '0_referencia': 'Referencia',
}

series = []

SOURCE_DIR = os.path.join(os.getcwd(), 'source_dirs')
os.chdir(SOURCE_DIR)
logger.debug(os.listdir(SOURCE_DIR))

for file in os.listdir(SOURCE_DIR):
    if os.path.isdir(file):
        logger.info('Found directory: %s' % file)
        if file in folder_name_map:
            logger.info('%s is in the name_folder_map!' % file)
            series.append(Series.from_folder(folder_name_map[file], file))
    else:
        print(f'{file} is not a directory')

print('Name;AvgMaxForce;ForceDeviation;AvgMaxSigma;SigmaDeviation;Display')
for seria in series:
    print(seria.name,
          seria.avg_max_force,
          seria.force_deviation,
          seria.avg_max_sigma,
          seria.sigma_deviation,
          'x', sep=';')

"""
for seria in series:
    print(seria.name)
    for name, data in zip(seria._all_original_name, seria.all_max_force):
        print(f'{name}: {data}')
    print(60 * '*')
"""
