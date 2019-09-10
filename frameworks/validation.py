# functions for validation and storing results
###########
# Imports #
###########
import datetime
from utilities import debugging as debug
import sklearn.metrics as sm
from utilities import config as con
import pandas as pd

#########
# Class #
#########
class model:

    def __init__(self, model_to_run, params, module):
        self.name = model_to_run + str(params)
        self.model_to_run = model_to_run
        self.params = params
        self.trained_model = None
        self.predicted = {'train': None, 'test': None, 'val': None}
        result_dic = {'accuracy': None, 'f-score': None, 'recall': None, 'precision': None, 'confusion_matrix': None}
        self.results = {'train': result_dic.copy(), 'test': result_dic.copy(), 'val': result_dic.copy()}
        self.module = module
        self.start_time = datetime.datetime.now()
        self.end_time = None
        self.run_time = None

    def validate(self):
        for val in con.data_splits:
            data_set = con.data_dic['y_' + val]
            predicted = self.predicted[val]
            self.results[val]['accuracy'] = sm.accuracy_score(data_set, predicted)
            self.results[val]['f-score'] = sm.f1_score(data_set, predicted)
            self.results[val]['precision'] = sm.precision_score(data_set, predicted)
            self.results[val]['recall'] = sm.recall_score(data_set, predicted)
            self.results[val]['confusion_matrix'] = sm.confusion_matrix(data_set, predicted)

        return

    def format_output(self):
        rows = []
        attrs = vars(self)

        data = []

        for val in con.data_splits:
            placeholder = {
                'name': attrs['name'],
                 'model_to_run': attrs['model_to_run'],
                 'params': str(attrs['params']),
                 'trained_model': attrs['trained_model'],
                 'start_time': str(attrs['start_time']),
                 'end_time': str(attrs['end_time']),
                 'run_time': str(attrs['run_time']),
                'data_set':val,
                 'accuracy': attrs['results'][val]['accuracy'],
                 'f-score': attrs['results'][val]['f-score'],
                 'recall': attrs['results'][val]['recall'],
                 'precision': attrs['results'][val]['precision'],
                 'confusion_matrix': attrs['results'][val]['confusion_matrix']
            }
            data.append(placeholder)

        df = pd.DataFrame(data)

        con.write_to_output_csv(df)
        return


    def store_result(self):
        self.end_time = datetime.datetime.now()
        self.run_time = self.end_time - self.start_time
        self.format_output()
        return

    def display_state(self):
        debug.debug_text('Model is Currently', level_4=True)
        attrs = vars(self)
        debug.debug_text(',\n'.join("%s: %s" % item for item in attrs.items()),results=True)
        return
