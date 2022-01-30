#############################################################
#
#                   DataExtractor
#
#############################################################

import csv
import sys
from config import DATA_COLUMN_TO_FIND, DATA_FILE_NAME, DATA_COLUMNS_CHR_TYPE

class DataExtractor:
    f_array_input = []
    f_array_output = []

    def __init__(self):        
        with open(DATA_FILE_NAME, 'r') as csv_file:
            f_reader = csv.DictReader(csv_file, delimiter = ';')
            f_array = list(f_reader)
            self.__set_output_and_input__(f_array)
        self.__to_float__(self.f_array_input)
        self.__to_float__(self.f_array_output)

        print(self.f_array_output)


    def __set_output_and_input__(self, array) :
        for line in range(0, len(array)) :
            self.f_array_output.append({})
            self.f_array_input.append({})

            for column in array[line].keys() :
                if column == DATA_COLUMN_TO_FIND :
                    self.f_array_output[line][column] = array[line][column]
                else :
                    self.f_array_input[line][column] = array[line][column]
        

    def __to_float__(self, array):
        if self.__column_is_in_array__(array, DATA_COLUMNS_CHR_TYPE) :
            for line in range(0, len(array)) :
                for column in DATA_COLUMNS_CHR_TYPE :            
                    try :
                        (array[line])[column] = ord((array[line])[column])
                    except Exception as e :
                        sys.exit("ERROR : DATA EXTRACTION : " + DATA_FILE_NAME + " line " + str(line) + " column " + str(column) + e)

    def __column_is_in_array__(self, array, columns) :
        for column in columns :
            for a_columns in array[0].keys() :
                if a_columns == column :
                    return True
        return False

    def get_input_line(self, line_number):
        return self.f_array_input[line_number]
    
    def get_output_line(self, line_number):
        return self.f_array_output[line_number]