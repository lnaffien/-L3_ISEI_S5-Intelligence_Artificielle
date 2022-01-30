#################################################################################################################
#                                                                                                               #
#                                               Perceptron                                                      #
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
from math import exp
from config import *

class Perceptron:
    bias = randrange(-10, 10)
    alpha = 0.1
    w = None            # liste des poids disponibles
    w_bias = randrange(-10, 10)

    def __init__(self, w):
        """ Initializes a new class instance.

        Args:
            w (list): list of weights. Does not contain the bias' weight. Needs to have as much weight as the number of inputs.
        """
        self.w = w
    
    def learn(self, data_input, data_output):
        """AI is creating summary for learn

        Args:
            data_input ([type], optional): [description]. Defaults to list.
            data_output ([type], optional): [description]. Defaults to list.
        """
        x = self.__x_calcul__(data_input)

        f = 0
        if PERCEPTRON_ACTIVATION_FUNCTION == SIGMOID :
            f = self.__f_calcul_sigmoid__(x)
        elif PERCEPTRON_ACTIVATION_FUNCTION == HYPERBOLIC_TANGENT :
            f = self.__f_calcul_hyperbolic_tangent__(x)
        else :
            exit("ERROR : CONFIG : PERCEPTRON_ACTIVATION_FUNCTION isn't a valid function.")

        #print("f(" + str(x) + ") = " + str(f))

        #     print("f(x) = x, so a weight update isn't necessary.")

        self.__weight_update__(data_input, data_output, f)

    def predict(self, data_input = list):
        return self.__f_calcul_sigmoid__(self.__x_calcul__(data_input))
        
    def __x_calcul__(self, data = list):
        """Calculate x value.

        Args:
            data ([type], optional): [description]. Defaults to list.

        Returns:
            [type]: [description]
        """
        x = self.w_bias # * self.bias
        for i in range(0, len(self.w)):
            x += self.w[i] * float(list(data.values())[i])
        return x

    def __f_calcul_sigmoid__(self, x):
        return (1 / (1 + exp(-x)))
    
    def __f_calcul_hyperbolic_tangent__(self, x):
        return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

    def __weight_update__(self, data_input = list, data_output = list, f = float):
        self.w_bias = self.w_bias + self.alpha * (float(list(data_output.values())[0]) - f) * self.bias
        for i in range(0, len(self.w)):
            #print("w" + str(i) + " = " + str(self.w[i]) + " + " + str(self.alpha) + " * (" + str(list(data_output.values())[0]) + " - " + str(f) + ") * " + str(list(data_input.values())[i]) )
            self.w[i] = self.w[i] + self.alpha * ( float(list(data_output.values())[0]) - f) * float(list(data_input.values())[i])
        #print(self.w)
        


    