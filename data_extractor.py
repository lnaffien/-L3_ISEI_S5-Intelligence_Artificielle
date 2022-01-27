#############################################################
#
#                   DataExtractor
#
#############################################################

from asyncore import read
import csv

class DataExtractor:
    DATA_FILE_NAME = "data_baby.csv"
    f_array = None

    def __init__(self):        
        with open(self.DATA_FILE_NAME, 'r') as csv_file:
          f_reader = csv.DictReader(csv_file, delimiter = ';')
          self.f_array = list(f_reader)

    def get_line(self, line_number):
        return self.f_array[line_number]
