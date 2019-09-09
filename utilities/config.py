# file defining the required configurations
###########
# Imports #
###########
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
paths = None
app_name = None

train_per = 0.7
test_per = 0.3
val_per = 0

######
# DB #
######


##############
# Parameters #
##############
target = 'Survived'

name_change_dic = {'Pclass': 'Class', 'SibSp': 'Sib', 'PassengerId': 'Id'}

required_field_list = ['Id', 'Class', 'Sex', 'Age', 'Sib', 'Fare', 'Embarked', 'Survived']

field_with_missing_dic = {'Age': 'Mean', 'Fare': 'Median'}

replace_field_with_dic = {
    'Sex': {'male': 0, 'female': 1}
}

one_hot_columns = ['Embarked']

index_column = 'Id'

data_dic = None

##########
# Models #
##########
# put in the models and parameters you would like
list_of_models = {
    'LogisticRegression' : [{'penalty':'elasticnet',
                            'C':0.9
                            },
                            {'C':0.6
                            }
                            ],
    'RandomForestClassifier': [{'n_estimators':150,
                               'max_depth':100
                               }]
}



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
    debug.debug_text('Collecting Paths', update=True)
    basePath = Path(__file__).parents[2]  # get base path
    paths = {'Base': basePath,
             'Input': (basePath / 'Input'),
             'Output': (basePath / 'Output'),
             'Raw_Files': (basePath / 'Raw_Files')}
    return


def init_system():
    global count, total_to_download, mode, app_name
    debug.debug_text('Initialising System', level_1=True)
    count, total_to_download = 1, 1

    collect_paths()

    debug.debug_text('Seting up logging file', update=True)
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    app_name = paths['Output'].parents[1].name
    logging_name = app_name + '.log'
    logging.basicConfig(filename=(paths['Output'] / logging_name).as_posix(),
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logging.info('Logging for {} stored at {}'.format(app_name, paths['Output']))

    return
