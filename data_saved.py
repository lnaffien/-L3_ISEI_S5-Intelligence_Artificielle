import csv
from config import DATA_COLUMNS_CHR_TYPE, DATA_RESULT_FILE_NAME

class DataSaved:
    def __init__(self, data) :
        with open(DATA_RESULT_FILE_NAME, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data, delimiter=';')
            writer.writeheader()

    def write_line(self, data) :
        with open(DATA_RESULT_FILE_NAME, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            self.__to_char__(data)
            writer.writerow(data.values())

    def __to_char__(self, data) :
        for column in DATA_COLUMNS_CHR_TYPE :
            data[column] = chr(data[column])

