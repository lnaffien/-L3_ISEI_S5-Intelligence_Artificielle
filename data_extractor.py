#############################################################
#
#                   DataExtractor
#
#############################################################

import csv
import sys
from config import DATA_FILE_NAME

class DataExtractor:
    f_array = None

    def __init__(self):        
        with open(DATA_FILE_NAME, 'r') as csv_file:
          f_reader = csv.DictReader(csv_file, delimiter = ';')
          self.f_array = list(f_reader)
        self.__to_float__()


    def __to_float__(self):
        for i in range(0, len(self.f_array)) : 
            try :
                (self.f_array[i])["Sexe"] = ord((self.f_array[i])["Sexe"])
            except Exception as e :
                sys.exit("ERROR : DATA EXTRACTION : " + DATA_FILE_NAME + " line " + str(i) + " " + e)


    def get_line(self, line_number):
        return self.f_array[line_number]