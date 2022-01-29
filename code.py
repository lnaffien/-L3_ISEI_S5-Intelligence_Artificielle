from hashlib import new
from random import random, randrange
from data_extractor import DataExtractor
from data_saved import DataSaved
from perceptron import Perceptron

data = DataExtractor()
w = []

for columnName in data.f_array[0]:
    w.append((randrange(0, 10)) / 10)

perceptron = Perceptron(w)
perceptron.exec_perceptron(data.get_line(4))

result = DataSaved(data.get_line(1))
result.write_line(data.get_line(1))

# w = [w0, w1, w2, w3] # semaine, sexe, poids, bias

# data = [0] * 3 # semaine, sexe, poids

# for i in range(497):
#     # Calcul de x        
#     # Calcul de f avec la sigmoide ou la tangeante hyperbolique
#     # Mise a jour des poids

