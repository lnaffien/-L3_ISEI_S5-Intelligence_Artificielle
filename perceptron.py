from random import randrange


class Perceptron:
    bias = randrange(-10, 10)
    w = None            # liste des poids disponibles
    w_bias = randrange(-10, 10)

    def __init__(self, w = list):
        self.w = w

    def x_calcul(self, data = list):
        # Calcul de x
        x = self.bias * self.w_bias

        for i in range(0, len(self.w)):
            x += self.w[i] * list(data.values())[i]
            print(x)

        # for weight in self.w:
        #     print("Calcul de x : OK")
        #    # x += weight * data[i] 
       
        # print (data[0])

    #def weight_update(w):
        


    