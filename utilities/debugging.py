###################
#                 #
#  #############  #
#  # Debugging #  #
#  #############  #
#                 #
###################
###########
# Imports #
###########
import logging


#############
# Functions #
#############
def header_level_1(text=None):
    # formatting
    length = len(text) + 4
    print('\n\n' + (length + 2) * '-')
    print('|' + length * ' ' + '|')
    print('|  ' + text + '  |')
    print('|' + length * ' ' + '|')
    print((length + 2) * '-')

    # output
    to_print = text
    logging.critical(to_print)

    return


def header_level_2(text=None):
    # formatting
    length = len(text)
    print('\n\n' + length * '-')
    print(text)
    print(length * '-')

    # output
    to_print = text
    logging.warning(to_print)

    return



def header_level_3(text=None):
    # formatting
    length = len(text)
    print('\n')
    print(text)
    print(length * '-')

    # output
    to_print = text
    logging.info(to_print)

    return



def header_level_4(text=None):
    # formatting
    length = len(text)
    print(text)
    print(length * '.')

    # output
    to_print = text
    logging.info(to_print)

    return



def process_update(text=None):
    # formatting
    print(text + '...')

    # output
    to_print = text
    logging.info(to_print)

    return



def success_message(text=None):
    # formatting
    if text is None:
        to_print = 'PROCESS COMPLETE - NO ERRORS\n'

    else:
        to_print = (text.upper() + ' -> Complete with no errors\n')

    # output
    print(to_print)
    logging.info(to_print)
    return



def error_message(text=None):
    # formatting
    if text is None:
        to_print = 'ERROR OCCURED!!!!!!!!'
    else:
        to_print = (text.upper() + ' -> FAILED there were errors\n')

    # output
    print(to_print)
    logging.CRITICAL(to_print)

    return


def debug_text(text=None
    ,level_1=False
    ,level_2=False
    ,level_3=False
    ,level_4=False
    ,update=False
    ,success=False
    ,error=False
    ):

    if level_1:
        header_level_1(text)

    if level_2:
        header_level_2(text)

    if level_3:
        header_level_3(text)

    if level_4:
        header_level_4(text)    

    if update:
        process_update(text)

    if success:
        success_message(text)

    if error:
        error_message(text)




    # add in logging


    return
