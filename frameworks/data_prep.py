# functions to prepare the data as required
###########
# Imports #
###########
from utilities import debugging as debug
from utilities import config as con
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd


#############
# Functions #
#############
# load file
def load_file(name, type):
    debug.debug_text('loading file', update=True)
    df = None
    loc = con.paths['Input'] / (name + '.' + type)
    if type == 'csv':
        return pd.read_csv(loc)
    if type == 'excel':
        return pd.read_excel(loc)
    else:
        debug.debug_text('Incorrect file type', error=True)
        exit()
    return df


# hot encode
def one_hot_encode(df, one_hot_columns=con.one_hot_columns):
    debug.debug_text('one hot encoding {}'.format(one_hot_columns), update=True)
    for column in one_hot_columns:
        dfDummies = pd.get_dummies(df[column], prefix=column)
        df = pd.concat([df, dfDummies], axis=1)
        df.drop(columns=[column], inplace=True)

    return df


# replace with 0, mean, median, or string
def replace_missing(df, field_with_missing_dic=con.field_with_missing_dic):
    debug.debug_text('replacing missing values for {}'.format(list(field_with_missing_dic.keys())), update=True)
    for key, value in field_with_missing_dic.items():
        if value == 'Mean':
            df[key].fillna(df[key].mean(), inplace=True)
        if value == 'Median':
            df[key].fillna(df[key].median(), inplace=True)
        if value == '0':
            df[key].fillna(0, inplace=True)
        else:
            df[key].fillna(value, inplace=True)

    return df


# replace values
def replace_values(df, replace_field_with_dic=con.replace_field_with_dic):
    debug.debug_text('replacing values for {}'.format(list(replace_field_with_dic.keys())), update=True)
    for key, value in replace_field_with_dic.items():
        df[key].replace(value, inplace=True)

    return df


# rename fields
def rename_column(df, name_dic=con.name_change_dic):
    debug.debug_text('renaming columns {}'.format(list(name_dic.keys())), update=True)
    return df.rename(columns=name_dic)


# remove fields
def remove_columns(df, required_field_list=con.required_field_list):
    to_remove = list(set(list(df.columns)) - set(required_field_list))
    debug.debug_text('removing columns {}'.format(to_remove), update=True)
    return df[required_field_list]


def change_index_column(df, index_column=con.index_column):
    debug.debug_text('resetting index to {}'.format(index_column), update=True)
    return df.set_index(index_column)


def normalise_fields(df):
    debug.debug_text('normalising fields', update=True)
    x = df.values  # returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    return pd.DataFrame(x_scaled, columns=df.columns, index=df.index)


# test train validation split
def split_data(df, target=con.target, train_per=con.train_per, test_per=con.test_per, val_per=con.val_per):
    debug.debug_text('Splitting Data: Train ({}), Test ({}), Val ({}) with a target field of {}'.format(
        train_per,
        test_per,
        val_per,
        target
    ), update=True)
    x = df.drop(columns=[target])
    y = df[target]

    x_train, x_test, x_val, y_train, y_test, y_val = '', '', '', '', '', ''

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=train_per)

    if val_per > 0:

        x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, train_size=test_per / (test_per + val_per))

        debug.debug_text(
            'Sizes ({}): x_train ({}), x_test ({}), x_val ({}), y_train ({}), y_test ({}), y_val ({})'.format(len(df),
                                                                                                              len(
                                                                                                                  x_train),
                                                                                                              len(
                                                                                                                  x_test),
                                                                                                              len(
                                                                                                                  x_val),
                                                                                                              len(
                                                                                                                  y_train),
                                                                                                              len(
                                                                                                                  y_test),
                                                                                                              len(
                                                                                                                  y_val)),
            update=True)

        return {'x_train': x_train, 'x_test': x_test, 'x_val': x_val, 'y_train': y_train, 'y_test': y_test,
                'y_val': y_val}
    else:
        debug.debug_text(
            'Sizes ({}): x_train ({}), x_test ({}), x_val ({}), y_train ({}), y_test ({}), y_val ({})'.format(len(df),
                                                                                                              len(
                                                                                                                  x_train),
                                                                                                              len(
                                                                                                                  x_test),
                                                                                                              len(
                                                                                                                  x_val),
                                                                                                              len(
                                                                                                                  y_train),
                                                                                                              len(
                                                                                                                  y_test),
                                                                                                              len(
                                                                                                                  y_val)),
            update=True)

        return {'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test}
