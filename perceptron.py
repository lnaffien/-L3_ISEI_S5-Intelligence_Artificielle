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
    w = None                        # list of availables weights
    w_bias = randrange(-10, 10)

    """ Initializes a new class instance.

        Args:
            w (list): list of weights. Does not contain the bias' weight. Needs to have as much weight as the number of inputs.
    """
    def __init__(self, w):        
        self.w = w
    
    
    """ Learn how to predict the given output with the given inputs.
            Will apply the function given in the config file as the activation function.

        Args:
            data_input (dict): inputs.
            data_output (dict): output.
    """
    def learn(self, data_input, data_output):        
        # Calculates x
        x = self.__x_calcul__(data_input)

        # Calculates f(x) with the activation function in the config file
        f = 0
        if PERCEPTRON_ACTIVATION_FUNCTION == SIGMOID :
            f = self.__f_calcul_sigmoid__(x)
        elif PERCEPTRON_ACTIVATION_FUNCTION == HYPERBOLIC_TANGENT :
            f = self.__f_calcul_hyperbolic_tangent__(x)
        else :
            exit("ERROR : CONFIG : PERCEPTRON_ACTIVATION_FUNCTION isn't a valid function.")

        # print("f(" + str(x) + ") = " + str(f))

        # print("A weight update isn't necessary.")

        # Weights update
        self.__weight_update__(data_input, data_output, f)


    """ Predicts an output according to the given input.

        Args:
            data_input (list): inputs.

        Returns:
            float: calculated output.
    """
    def predict(self, data_input):        
        f = 0
        if PERCEPTRON_ACTIVATION_FUNCTION == SIGMOID :
            return self.__f_calcul_sigmoid__(self.__x_calcul__(data_input))
        elif PERCEPTRON_ACTIVATION_FUNCTION == HYPERBOLIC_TANGENT :
            return self.__f_calcul_hyperbolic_tangent__(self.__x_calcul__(data_input))
        else :
            exit("ERROR : CONFIG : PERCEPTRON_ACTIVATION_FUNCTION isn't a valid function.")
        

    """Calculates x value.

        Args:
            data (dict): data inputs.

        Returns:
            float: x.
    """
    def __x_calcul__(self, data):        
        x = self.w_bias * self.bias
        for i in range(0, len(self.w)):
            x += self.w[i] * float(list(data.values())[i])
        return x


    """Activation function with the sigmoid.

        Args:
            x (float): x.

        Returns:
            float: results of the activation function.
    """
    def __f_calcul_sigmoid__(self, x):        
        return (1 / (1 + exp(-x)))
    

    """Activation function with the hyperbolic tangent.

        Args:
            x (float): x.

        Returns:
            float: results of the activation function.
    """
    def __f_calcul_hyperbolic_tangent__(self, x):        
        return ((exp(x) - exp(-x)) / (exp(x) + exp(-x)))


    """Updates all the weights

        Args:
            data_input (dict): inputs.
            data_output (dict): expected result.
            f (float): result of the activation function.
    """
    def __weight_update__(self, data_input, data_output, f):
        self.w_bias = self.w_bias + self.alpha * (float(list(data_output.values())[0]) - f) * self.bias
        for i in range(0, len(self.w)):
            #print("w" + str(i) + " = " + str(self.w[i]) + " + " + str(self.alpha) + " * (" + str(list(data_output.values())[0]) + " - " + str(f) + ") * " + str(list(data_input.values())[i]) )
            self.w[i] = self.w[i] + self.alpha * ( float(list(data_output.values())[0]) - f) * float(list(data_input.values())[i])  