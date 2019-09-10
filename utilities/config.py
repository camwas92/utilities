# file defining the required configurations
###########
# Imports #
###########
import logging
import pandas as pd
from utilities import debugging as debug
from frameworks import validation as v
import os
import csv

###################
#                 #
#  #############  #
#  # Constants #  #
#  #############  #
#                 #
###################
debugging = False

error_flag = False

paths = None
app_name = None

train_per = 0.7
test_per = 0.3
val_per = 0.0

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

data_splits = None

##########
# Models #
##########
# put in the models and parameters you would like
models_to_evaulate = {
    'LogisticRegression|sklearn.linear_model': [{'C': 0.9
                                                 },
                                                {'C': 0.6
                                                 }
                                                ],
    'RandomForestClassifier|sklearn.ensemble': [{'n_estimators': 150,
                                                 'max_depth': 100
                                                 }],
    'KMeans|sklearn.cluster': [{'n_clusters': 2}],
    'MLPClassifier|sklearn.neural_network': [{}]
}

models = []

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


def create_models():
    global models
    debug.debug_text('Creating list of models', update=True)
    for key, values in models_to_evaulate.items():
        for value in values:
            model_to_run, module = key.split('|')
            models.append(v.model(model_to_run=model_to_run, params=value, module=module))


def check_dir(file_name):
    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_to_output_csv(df):
    file_name = app_name + '_output.csv'
    check_dir((paths['Output'] / file_name).as_posix())

    with open((paths['Output'] / file_name).as_posix(), 'a') as f:
        df.to_csv(f, header=f.tell() == 0, sep=',', index=False)

    f.close()

    count = len(df)
    debug.debug_text("{} record saved to {}".format(count, file_name), update=True)

    return


def init_system():
    global count, total_to_download, mode, app_name, data_splits
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

    create_models()

    # track what data needs to be produced and stored
    if val_per > 0:
        data_splits = ['train', 'test', 'val']
    else:
        data_splits = ['train', 'test']

    # set up output csv

    return
