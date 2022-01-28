#############################################################
#
#                   DataExtractor
#
#############################################################

from ast import Try
from asyncore import read
import csv
from operator import le
from shutil import ExecError
import string
import sys

class DataExtractor:
    DATA_FILE_NAME = "data_baby.csv"
    f_array = None

    def __init__(self):        
        with open(self.DATA_FILE_NAME, 'r') as csv_file:
          f_reader = csv.DictReader(csv_file, delimiter = ';')
          self.f_array = list(f_reader)
        self.__to_float__()


    def __to_float__(self):
        for i in range(0, len(self.f_array)) : 
            try :
                (self.f_array[i])["Sexe"] = ord((self.f_array[1])["Sexe"])
            except Exception :
                sys.exit("ERROR : DATA EXTRACTION : " + self.DATA_FILE_NAME + " line " + str(i) + " there's str instead of char data in the file.")


    def get_line(self, line_number):
        return self.f_array[line_number]