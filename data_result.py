import csv
from config import DATA_COLUMN_TO_FIND, DATA_COLUMNS_CHR_TYPE, DATA_RESULT_FILE_NAME

class DataResult:
    def __init__(self, data_input, data_output) :
        columns_name = list(data_input)
        for key in data_output :
            columns_name.append(key)

        with open(DATA_RESULT_FILE_NAME, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns_name, delimiter=';')
            writer.writeheader()

    def write_line(self, data_input, data_output) :
        data = data_input
        data[DATA_COLUMN_TO_FIND] = data_output
        print(data)

        with open(DATA_RESULT_FILE_NAME, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            self.__to_char__(data)
            writer.writerow(data.values())

    def __to_char__(self, data) :
        for column in DATA_COLUMNS_CHR_TYPE :
            data[column] = chr(data[column])



