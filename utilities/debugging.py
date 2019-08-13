###################
#                 #
#  #############  #
#  # Debugging #  #
#  #############  #
#                 #
###################
import logging



def header_level_1(text=None):
    length = len(text) + 4
    print('\n\n' + (length + 2) * '-')
    print('|' + length * ' ' + '|')
    print('|  ' + text + '  |')
    print('|' + length * ' ' + '|')
    print((length + 2) * '-')
    return


def header_level_2(text=None):
    length = len(text)
    print('\n\n' + length * '-')
    print(text)
    print(length * '-')
    return



def header_level_3(text=None):
    length = len(text)
    print('\n')
    print(text)
    print(length * '-')
    return



def header_level_4(text=None):
    length = len(text)
    print(text)
    print(length * '.')
    return



def process_update(text=None):
    print(text + '...')



def success_message(text=None):
    if text is None:
        print('PROCESS COMPLETE - NO ERRORS\n')
    else:
        print(text.upper() + ' -> Complete with no errors\n')
    return



def error_message(text=None):
    to_print = ''
    if text is None:
        to_print = 'ERROR OCCURED!!!!!!!!'
    else:
        to_print = text.upper() + ' -> FAILED there were errors\n'
    print(to_print)
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
