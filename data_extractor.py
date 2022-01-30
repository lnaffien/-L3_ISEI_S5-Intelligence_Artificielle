#################################################################################################################
#                                                                                                               #
#                                               DataExtractor                                                   #
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
import sys
from config import DATA_COLUMN_TO_FIND, DATA_FILE_NAME, DATA_COLUMNS_CHR_TYPE

class DataExtractor:
    f_array_input = []
    f_array_output = []

    """ Initializes a new class instance.
        Read data from the data's file and store it into 2 lists, one with the inputs and the other with the outputs.
        The file name is taken from the config file.
    """
    def __init__(self):        
        with open(DATA_FILE_NAME, 'r') as csv_file:
            f_reader = csv.DictReader(csv_file, delimiter = ';')
            f_array = list(f_reader)
            self.__set_output_and_input__(f_array)
        self.__to_float__(self.f_array_input)
        self.__to_float__(self.f_array_output)


    """ Split extracted data into 2 list. One contains the input, the other contains the output.
        Ouput column's name is in the config file.

        Args:
            array (list): list to split.
    """
    def __set_output_and_input__(self, array) :
        for line in range(0, len(array)) :
            # Creates new lines into input and output lists
            self.f_array_output.append({})
            self.f_array_input.append({})

            # Short data into the 2 lists
            for column in array[line].keys() :
                if column == DATA_COLUMN_TO_FIND :
                    self.f_array_output[line][column] = array[line][column]
                else :
                    self.f_array_input[line][column] = array[line][column]
    

    """ Converts all chr data from specified columns to float.
        Columns to convert are in the config file.

        Args:
            array (list): data to convert.
    """
    def __to_float__(self, array):
        
        if self.__column_is_in_array__(array, DATA_COLUMNS_CHR_TYPE) :
            for line in range(0, len(array)) :
                for column in DATA_COLUMNS_CHR_TYPE :            
                    try :
                        (array[line])[column] = ord((array[line])[column])
                    # Exit on error if the data isn't a convertible type, like a string
                    except Exception as e :
                        sys.exit("ERROR : DATA EXTRACTION : " + DATA_FILE_NAME + " line " + str(line) + " column " + str(column) + e)


    """ Check if the given list as at least one column from the given ones.

        Args:
            array (list): list to check.
            columns (list): column's name to compare with the list's ones.

        Returns:
            bool: True if at least one of the given columns is in the list, False otherwise.
    """
    def __column_is_in_array__(self, array, columns) :
        for column in columns :
            for a_columns in array[0].keys() :
                if a_columns == column :
                    return True
        return False
    

    """ Get input(s) of a specified line.

        Args:
            line_number (int): specific line.

        Returns:
            dict: input(s) of the specified line.
    """
    def get_input_line(self, line_number):
        return self.f_array_input[line_number]

    
    """ Get output of a specified line.

        Args:
            line_number (int): specific line.

        Returns:
            dict: output of the specified line.
    """
    def get_output_line(self, line_number):        
        return self.f_array_output[line_number]