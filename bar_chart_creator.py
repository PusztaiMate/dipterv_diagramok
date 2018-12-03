"""Creates a bar-chart from the input data"""
import matplotlib.pyplot as plt
import numpy as np
import random
import logging


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

def draw_chart(y_name: str,
     x_names: list,
     avgs: list,
     stdevs: list,
     title: str) -> None:
    # check if the inputs are the same length
    if len(x_names) != len(avgs) or len(avgs) != len(stdevs):
        raise RuntimeError('The length of the given lists are not equal.')
    index = np.arange(len(avgs))
    width = 1/1.5

    bar_colors = Utilities.create_color_scale(len(avgs),
                                              color_from=(0.3, 0.6, 0.9),
                                              color_to=(0.8, 1, 0.1))
    plt.bar(index, avgs, width, yerr=stdevs, color=bar_colors)
    plt.ylabel(y_name)
    plt.xticks(index, x_names)
    plt.title(title)
    plt.show()

class Utilities:

    @staticmethod
    def create_color_scale(num_needed: int,
                           color_from: tuple=(0, 1, 0),
                           color_to: tuple=(0, 0, 1)) -> list:
        """create colors from green to blue"""
        if num_needed == 0:
            return None
        elif num_needed == 1:
            return [color_from]
        elif num_needed == 2:
            return [color_from, color_to]
        
        r_f, g_f, b_f = color_from
        r_t, g_t, b_t = color_to

        r_diff = r_t - r_f
        g_diff = g_t - g_f
        b_diff = b_t - b_f

        # calculate steps
        r_step = r_diff / (num_needed - 1)
        g_step = g_diff / (num_needed - 1)
        b_step = b_diff / (num_needed - 1)

        return [(r_f + x*r_step, g_f + x*g_step, b_f + x*b_step) for x in range(num_needed)]


if __name__ == '__main__':
    # create dummy data
    dummy_x_name = 'Force [N]'
    dummy_y_names = ['10/20', '20/10', '10m%', '25m%', '40m%']
    dummy_avgs = [76.3, 98.2, 132.2, 41.7, 27.0]
    dummy_stdevs = [12.2, 19.9, 23.4, 9.8, 5.6]
    dummy_title = 'Avarage forces and deviations'
    draw_chart(dummy_x_name, dummy_y_names, dummy_avgs, dummy_stdevs, dummy_title)