# file defining the required configurations

import logging

import pandas as pd

from utilities import debugging as debug

###################
#                 #
#  #############  #
#  # Constants #  #
#  #############  #
#                 #
###################


######
# DB #
######


##############
# Parameters #
##############



########################
#                      #
#  ##################  #
#  # Initialisation #  #
#  ##################  #
#                      #
########################
from pathlib import Path


def collect_paths():
    global paths
    debug.process_update('Collecting Paths')
    basePath = Path(__file__).parents[3]  # get base path
    paths = {'Base': basePath,
             'Input': (basePath / 'Input'),
             'Output': (basePath / 'Output'),
             'Raw_Files': (basePath / 'Raw_Files')}
    return



def init_system():
    global count, total_to_download, mode
    debug.header_level_1('Initialising System')
    count, total_to_download = 1, 1

    collect_paths()

    debug.process_update('Seting up logging file')
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=(paths['Output'] / 'RegXplorer.log').as_posix(),
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logging.info('Running RegXplorer on {}'.format(mode))


    return
