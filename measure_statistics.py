import os
import logging
from statistics import mean, stdev
from tra_data_loader import load_tra, DataPoint


logger = logging.getLogger(__name__)


class TRA:
    '''Result class to hold the computational statistics
    and results about a TRA'''

    def __init__(self, name: str, data: list, original_name:str=None):
        self.name = name
        self.max_force = self._calc_max_force(data)  # N
        self.base_area = 120  # m^2
        self.max_sigma = self._calc_max_sigma()  # MPa
        self._data = data
        self.original_name = original_name or 'NoNameGiven'

    def _calc_max_force(self, data: list) -> float:
        return max([datapoint.force for datapoint in data])
    
    def _calc_max_sigma(self) -> float:
        return self.max_force / self.base_area

    def get_data_as_two_list(self) -> tuple:
        '''returns strains, forces tuple'''
        strains = [datapoint.strain for datapoint in self._data]
        forces = [datapoint.force for datapoint in self._data]
        return strains, forces


class Series:
    '''Holds multiple series and can provide
    statistics about the series as a whole.'''

    def __init__(self, name: str, list_of_tra: list):
        self.tra_list = list_of_tra
        self.name = name

    @property
    def avg_max_force(self):
        return mean([tra.max_force for tra in self.tra_list])

    @property
    def force_deviation(self):
        return stdev(self.all_max_force)

    @property
    def sigma_deviation(self):
        return stdev(self.all_max_sigma)

    @property
    def avg_max_sigma(self):
        return mean([tra.max_sigma for tra in self.tra_list])

    @property
    def all_max_sigma(self):
        return [tra.max_sigma for tra in self.tra_list]

    @property
    def all_max_force(self):
        return [tra.max_force for tra in self.tra_list]

    @property
    def _all_original_name(self):
        return [tra.original_name for tra in self.tra_list]

    @classmethod
    def from_folder(cls, name: str, folder_path: str):
        tra_filenames = get_tra_from_folder(folder_path)
        tra_files = [load_tra(f) for f in tra_filenames]
        return cls(name, [TRA(str(i), tra, tra_filenames[i]) for i, tra in enumerate(tra_files)])


def get_tra_from_folder(folder_path: str):
    files = os.listdir(folder_path)
    tra_files = []
    for file in files:
        _, ext = os.path.splitext(file)
        if ext == '.TRA':
            tra_files.append(os.path.join(folder_path, file))
    return tra_files


if __name__ == '__main__':
    dirname = os.path.join(os.getcwd(), 'test_data')
    series = Series.from_folder('Test series', dirname)

    print('Name,AvgMaxForce,ForceDeviation,AvgMaxSigma,SigmaDeviation,Display')
    print(series.avg_max_force,
          series.force_deviation,
          series.avg_max_sigma,
          series.sigma_deviation,
          'x', sep=',')
