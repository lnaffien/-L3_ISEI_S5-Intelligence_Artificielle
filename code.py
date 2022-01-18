from math import exp
from random import random

def main():
    delta = 0
    f = 0
    x = 0
    bias = random()

    w0 = random()
    w1 = random()
    w2 = random()
    w3 = random()
    w = [w0, w1, w2, w3] # semaine, sexe, poids, bias
    data = [0] * 3 # semaine, sexe, poids

    for i in range(497):
        # Calcul de x
        x = bias * w[3]
        for j in data:
            x += w[j] * data[j]
        print("Calcul de x : OK")
        
        # Calcul de f avec la sigmoide
        f = 1 / (1 + exp(-x))
        print("Calcul de f (sigmoide) : OK")

        if f != x : 
            # Mise a jour des poids
                for j in data:
                    w[j] = w[j] + delta * (data[2] - f) * data[j]
                w[3] = w[3] + delta * ( data[2] - f) * bias
                print("Mise a jour des poids : OK")
        else : 
            print("f(x) = x, une mise a jour des poids n'est donc pas necessaire.")
