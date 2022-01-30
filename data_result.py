#################################################################################################################
#                                                                                                               #
#                                               DataResult                                                      #
#                                                       by NAFFIEN Lucie (January 2022)                         #
#                                                                                                               #
# This module is a part of the project made for the "Artificial Intelligence" course, teached by M. DAACHI.     #
# It is a part of the 3rd Bachelor's Computer Science specialised for Embedded and Interactive Systems year,    #
# at University Paris 8.                                                                                        #
#                                                                                                               #
# GitHub link for the full project : https://github.com/lnaffien/L3_ISEI_S5-Intelligence_Artificielle           #
#                                                                                                               #
#################################################################################################################

import csv
from config import DATA_COLUMN_TO_FIND, DATA_COLUMNS_CHR_TYPE, DATA_RESULT_FILE_NAME

class DataResult:

    """ Initializes a new class instance.
        If the file doesn't exist, creates a new one and initializes columns' name.
        If not, deletes all the previous content.
        The file name is taken from the config file.

        Args :
            data_input (dict): data input used to calculate the output.
            data_output (dict): output to calculate.
    """
    def __init__(self, data_input, data_output) :
        # Merges output and input into a single dict
        columns_name = list(data_input)
        for key in data_output :
            columns_name.append(key)

        # Delete alle the previous content and write the columns' name
        with open(DATA_RESULT_FILE_NAME, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns_name, delimiter=';')
            writer.writeheader()

    
    """ Writes a new line into the result file.

        Args:
            data_input (dict): data input used to calculate the output.
            data_output (float): calculated output.
    """
    def write_line(self, data_input, data_output) :     
        # Merges output and input into a single dict
        data = data_input
        data[DATA_COLUMN_TO_FIND] = data_output

        # Writes data
        with open(DATA_RESULT_FILE_NAME, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            self.__to_char__(data)
            writer.writerow(data.values())

    
    """ Converts specified data column into char from their ASCII code.

        Args:
            data (dict): result data.
    """
    def __to_char__(self, data) :
        for column in DATA_COLUMNS_CHR_TYPE :
            data[column] = chr(int(data[column]))