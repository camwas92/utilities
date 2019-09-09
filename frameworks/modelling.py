# functions for modelling
###########
# Imports #
###########
from utilities import config as con
from utilities import debugging as debug

#############
# Functions #
#############

def train_model(single_model):
    debug.debug_text('Training {} with {}'.format(single_model.model_to_run,single_model.params),update=True)
    # todo
    single_model.trained_model = None
    return

def predict_results(single_model):
    debug.debug_text('Prdicting {} with {}'.format(single_model.model_to_run,single_model.params),update=True)
    # predict train
    # todo

    if con.val_per > 0:
        # predict validation
        #todo
        pass
    return

def validate_model(single_model):
    debug.debug_text('Validating {}'.format(single_model.model_to_run),update=True)
    single_model.validate()
    return

def store_results(single_model):
    debug.debug_text('Storing results for {}'.format(single_model.model_to_run),update=True)
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

