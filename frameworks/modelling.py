# functions for modelling
###########
# Imports #
###########
from utilities import config as con
from utilities import debugging as debug

#############
# Functions #
#############

def train_model(model,params):
    debug.debug_text('Training {} with {}'.format(model,params),update=True)
    return

def validate_model(model):
    debug.debug_text('validating {}'.format(model),update=True)
    return


def run_models():
    for model in con.list_of_models:
        for params in con.list_of_models[model]:
            debug.debug_text('Running model -> {} ... parameters {}'.format(model,params),level_2=True)
            train_model(model,params)
            validate_model(model)
    return

