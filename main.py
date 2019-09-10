# main file, undertakes the core components

from frameworks import data_prep as dp
from frameworks import modelling as m
from frameworks import validation as v
from utilities import config as con
from utilities import debugging as debug

# initialise system
con.init_system()

#################
# DATA CLEANING #
#################
debug.debug_text('Pre-processing Data', level_1=True)
# 1) Load data
df = dp.load_file(name='titanic', type='csv')
# 2) rename fields
df = dp.rename_column(df)
# 3) remove fields
df = dp.remove_columns(df)
# 4) replace missing
df = dp.replace_missing(df)
# 5) replace values
df = dp.replace_values(df)
# 6) one hot encoding
df = dp.one_hot_encode(df)
# 7) change index column
df = dp.change_index_column(df)
# 8) normalise fields
df = dp.normalise_fields(df)
# 9)split data
con.data_dic = dp.split_data(df)

#############################
# MODELLLING and VALIDATION #
#############################
debug.debug_text('Modelling', level_1=True)
m.run_models()
# complete
debug.debug_text('{} is completed'.format(con.app_name),error=con.error_flag,success= not con.error_flag)
