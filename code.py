from random import randrange
from config import DATA_MAX_LEARNING_ROW, LAYER_NUMBER
from data_extractor import DataExtractor
from data_result import DataResult
from perceptron import Perceptron

data = DataExtractor()
result_data = DataResult(data.get_input_line(0), data.get_output_line(0))

for i  in range(0, LAYER_NUMBER) :
    w = []
    for columnName in data.f_array_input[0]:
        w.append((randrange(0, 10)) / 10)

    perceptron = Perceptron(w)
    for line in range(0, DATA_MAX_LEARNING_ROW - 1) :
        perceptron.learn(data.get_input_line(line), data.get_output_line(line))

for line in range(DATA_MAX_LEARNING_ROW, len(data.f_array_input)) :
    res = perceptron.predict(data.get_input_line(line))
    result_data.write_line(data.get_input_line(line), res)

# w = [w0, w1, w2, w3] # semaine, sexe, poids, bias

# for i in range(497):
#     # Calcul de x        
#     # Calcul de f avec la sigmoide ou la tangeante hyperbolique
#     # Mise a jour des poids

