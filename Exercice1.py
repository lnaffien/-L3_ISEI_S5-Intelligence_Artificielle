from random import seed, random
import math
from pylab import *

delta = 0.1
k = 0
x = array([3, 2, 1, 1],
        [1, 1, 1, 1],
        [1, 2, 3, 0.2])
#y = array([0, 1, 1, 1]) #ou logique
y = array([0, 1, 1, 0]) #ou exclusif
#y = array([0, 0, 0, 0]) #et logique

w1 = random()
w2 = random() #-random()
w3 = random() #-random()
w0 = random() #-random()
w = ([w1], [w2], [w3], [w0])
yc = np.dot(x, w) #calcul de la sortie du RN
print yc

#print w
#print y
#print x
for i in range(4) :
    print x[i, 1]
for i in range(4) :
    if(yc[i] > 0) :
        yc[i]=1
    else:
        yc[i]=0
print yc

w0 = [w0]
w1 = [w1]
w2 = [w2]
w3 = [w3]
while k < 50 :
    for i in range(3) : 
        w0 = w0 + delta * (y[i] - yc[i] * x[i, 3])
        w1 = w1 + delta * (y[i] - yc[i] * x[i, 0])
        w2 = w2 + delta * (y[i] - yc[i] * x[i, 1])
        w3 = w3 + delta * (y[i] - yc[i] * x[i, 2])
    k = k + 1
    w = ([w1, w2, w3, w0])
    yc = np.dot(x, w) #calcul de la sortie du RN

    for i in range(3) : 
        if(yc[i] > 0) :
        yc[i]=1
    else:
        yc[i]=0
print yc
#w0.append(w0)
#w1.append(w1)
#w2.append(w2)
#w3.append(w3)


#print size(w0)
#plt.xlim(-5, 50)
#plt.ylim(-1.5, )
#print yc
print w