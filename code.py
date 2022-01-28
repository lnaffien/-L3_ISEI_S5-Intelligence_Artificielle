from hashlib import new
from math import exp
from random import random, randrange
from data_extractor import DataExtractor
from perceptron import Perceptron

data = DataExtractor()
w = []

for columnName in data.f_array[0]:
    w.append(randrange(-10, 10))

# perceptron = Perceptron(w)

# temp = data.get_line(0).values()
# print(temp)
#perceptron.x_calcul(data.get_line(0))

# w = [w0, w1, w2, w3] # semaine, sexe, poids, bias


# delta = 0
# f = 0
# x = 0
# # bias = random()



# data = [0] * 3 # semaine, sexe, poids

# for i in range(497):
#     # Calcul de x
        
#     # Calcul de f avec la sigmoide
#     f = 1 / (1 + exp(-x))
#     print("Calcul de f (sigmoide) : OK")

#     if f != x : 
#         # Mise a jour des poids
#             for j in data:
#                 w[j] = w[j] + delta * (data[2] - f) * data[j]
#             w[3] = w[3] + delta * ( data[2] - f) * bias
#             print("Mise a jour des poids : OK")
#     else : 
#         print("f(x) = x, une mise a jour des poids n'est donc pas necessaire.")

