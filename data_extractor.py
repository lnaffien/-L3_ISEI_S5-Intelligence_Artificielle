from asyncore import read
import csv

DATA_FILE_NAME = "data_baby.csv"
f_array = None

class DataExtractor:

    f = ''
    line = 0

    def __init__(self):        
        with open(DATA_FILE_NAME, 'r') as csv_file:
          f_reader = csv.DictReader(csv_file, delimiter = ';')
          f_array = list(f_reader)

    def get_line(self, line_number):
        return f_array[line_number]
