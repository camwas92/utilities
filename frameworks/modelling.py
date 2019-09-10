# functions for modelling
###########
# Imports #
###########
from utilities import config as con
from utilities import debugging as debug
import importlib
# models
from sklearn.linear_model import LogisticRegression


#############
# Functions #
#############

def train_model(single_model):
    debug.debug_text('Training {} with {}'.format(single_model.model_to_run, single_model.params), update=True)
    # train model based on class values
    module = importlib.import_module(single_model.module)
    model_to_run = getattr(module, single_model.model_to_run)
    # run model based on function and train
    single_model.trained_model = model_to_run(**single_model.params).fit(con.data_dic['x_train'],
                                                                         con.data_dic['y_train'])
    return


def predict_results(single_model):
    debug.debug_text('Predicting {} with {}'.format(single_model.model_to_run, single_model.params), update=True)
    # predict
    for val in con.data_splits:
        single_model.predicted[val] = single_model.trained_model.predict(con.data_dic['x_'+val])

    return


def validate_model(single_model):
    debug.debug_text('Validating {}'.format(single_model.model_to_run), update=True)
    single_model.validate()
    return


def store_results(single_model):
    debug.debug_text('Storing results for {}'.format(single_model.model_to_run), update=True)
    single_model.store_result()
    single_model.display_state()
    return


def run_models():
    for single_model in con.models:
        debug.debug_text('Running model -> {}'.format(single_model.name), level_2=True)
        train_model(single_model)
        predict_results(single_model)
        validate_model(single_model)
        store_results(single_model)
    return
