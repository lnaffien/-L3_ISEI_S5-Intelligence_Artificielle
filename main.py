#################################################################################################################
#                                                                                                               #
#                                               Main                                                            #
#                                                       by NAFFIEN Lucie (January 2022)                         #
#                                                                                                               #
# This module is a part of the project made for the "Artificial Intelligence" course, teached by M. DAACHI.     #
# It is a part of the 3rd Bachelor's Computer Science specialised for Embedded and Interactive Systems year,    #
# at University Paris 8.                                                                                        #
#                                                                                                               #
# GitHub link for the full project : https://github.com/lnaffien/L3_ISEI_S5-Intelligence_Artificielle           #
#                                                                                                               #
#################################################################################################################

from random import randrange
from config import DATA_MAX_LEARNING_ROW, LAYER_NUMBER
from data_extractor import DataExtractor
from data_result import DataResult
from perceptron import Perceptron

# Initializes data files
data = DataExtractor()
result_data = DataResult(data.get_input_line(0), data.get_output_line(0))

for i  in range(0, LAYER_NUMBER) :
    # Initializes weights
    w = []
    for columnName in data.f_array_input[0]:
        w.append((randrange(0, 10)) / 10)

    # Learning phase. Will use all the data from 0 to the specified line in the config file
    perceptron = Perceptron(w)
    for line in range(0, DATA_MAX_LEARNING_ROW - 1) :
        perceptron.learn(data.get_input_line(line), data.get_output_line(line))

# Prediction phase. Will use all the data from specified line in the config file to the last data line
for line in range(DATA_MAX_LEARNING_ROW, len(data.f_array_input)) :
    res = perceptron.predict(data.get_input_line(line))
    # Writes result into a result file. Its name is given in the config file
    result_data.write_line(data.get_input_line(line), res)