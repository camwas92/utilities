# functions for validation and storing results
###########
# Imports #
###########
import datetime
from utilities import debugging as debug
import sklearn.metrics as sm
from utilities import config as con

#########
# Class #
#########
class model:

    def __init__(self, model_to_run,params):
        self.name = model_to_run + str(params)
        self.model_to_run = model_to_run
        self.params = params
        self.trained_model = None
        self.predicted = {'train':None,'test':None,'val':None}
        result_dic = {'accuracy':None,'f-score':None,'recall':None,'precision':None}
        self.results = {'train':result_dic,'test':result_dic,'val':result_dic}
        self.start_time = datetime.datetime.now()
        self.end_time = None

    def validate(self):
        if con.val_per > 0:
            validate_list = ['train', 'test', 'val']
        else:
            validate_list = ['train', 'test']
        # for test
        for val in validate_list:
            data_set = con.data_dic['y_'+val]
            predicted = self.predicted[val]
            self.results[val]['accuracy'] = sm.accuracy_score(data_set,predicted)
            self.results[val]['f-score'] = sm.f1_score(data_set,self.predicted)
            self.results[val]['precision'] = sm.precision_score(data_set,predicted)
            self.results[val]['recall'] = sm.recall_score(data_set,predicted)


        return

    def store_result(self):
        self.end_time = datetime.datetime.now()
        #todo
        return

    def display_state(self):
        debug.debug_text('Model is Currently',level_4=True)
        attrs = vars(self)
        print (',\n'.join("%s: %s" % item for item in attrs.items()))
        return



