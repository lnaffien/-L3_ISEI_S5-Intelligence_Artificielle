from random import randrange
from math import exp
from config import *

class Perceptron:
    bias = randrange(-10, 10)
    alpha = 0.1
    w = None            # liste des poids disponibles
    w_bias = randrange(-10, 10)

    def __init__(self, w = list):
        self.w = w
    
    def exec_perceptron(self, data = list):
        x = self.__x_calcul__(data)

        f = 0
        if PERCEPTRON_ACTIVATION_FUNCTION == SIGMOID :
            f = self.__f_calcul_sigmoid__(x)
        elif PERCEPTRON_ACTIVATION_FUNCTION == HYPERBOLIC_TANGENT :
            f = self.__f_calcul_hyperbolic_tangent__(x)
        else :
            exit("ERROR : CONFIG : PERCEPTRON_ACTIVATION_FUNCTION isn't a valid function.")

        print("f(" + str(x) + ") = " + str(f))

        #     print("f(x) = x, so a weight update isn't necessary.")

        self.__weight_update__(data, f)        

        
    def __x_calcul__(self, data = list):
        x = self.bias * self.w_bias
        for i in range(0, len(self.w)):
            x += self.w[i] * float(list(data.values())[i])
        return x

    def __f_calcul_sigmoid__(self, x):
        return (1 / (1 + exp(-x)))
    
    def __f_calcul_hyperbolic_tangent__(self, x):
        return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

    def __weight_update__(self, data = list, f = float):
        self.w_bias = self.w_bias + self.alpha * ( - f) * self.bias
        print(self.w)
        for i in range(0, len(self.w)):
            print("w" + str(i) + " = " + str(self.w[i]) + " + " + str(self.alpha) + " * (" + str(f) + " - " + str(f) + ") * " + str(list(data.values())[i]) )
            self.w[i] = self.w[i] + self.alpha * ( - f) * float(list(data.values())[i])
        print(self.w)
        


    