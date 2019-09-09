# main file, undertakes the core components

from frameworks import data_prep as dp
from frameworks import modelling as m
from frameworks import validation as v
from utilities import config as con
from utilities import debugging as debug


con.init_system()


#################
# DATA CLEANING #
#################
debug.debug_text('Preprocessing Data',level_1=True)

df = dp.load_file(name='titanic',type='csv')

# rename fields
df = dp.rename_column(df)

# remove fields
df = dp.remove_columns(df)

# replace missing
df = dp.replace_missing(df)

# replace values
df = dp.replace_values(df)

# one hot encoding
df = dp.one_hot_encode(df)

# change index column
df = dp.change_index_column(df)

# normalise fields
df = dp.normalise_fields(df)

# split data
con.data_dic = dp.split_data(df)


##############
# MODELLLING #
##############
debug.debug_text('Modelling',level_1=True)
m.run_models()