#############################################################
#
#                   DataExtractor
#
#############################################################

import csv
import sys
from config import DATA_FILE_NAME, DATA_COLUMNS_CHR_TYPE

class DataExtractor:
    f_array = None

    def __init__(self):        
        with open(DATA_FILE_NAME, 'r') as csv_file:
          f_reader = csv.DictReader(csv_file, delimiter = ';')
          self.f_array = list(f_reader)
        self.__to_float__()


    def __to_float__(self):
        for line in range(0, len(self.f_array)) :
            for column in DATA_COLUMNS_CHR_TYPE :            
                try :
                    (self.f_array[line])[column] = ord((self.f_array[line])[column])
                except Exception as e :
                    sys.exit("ERROR : DATA EXTRACTION : " + DATA_FILE_NAME + " line " + str(line) + " column " + str(column) + e)


    def get_line(self, line_number):
        return self.f_array[line_number]