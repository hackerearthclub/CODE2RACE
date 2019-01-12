import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import math

xmin = -4
xmax = 4
x = np.arange(start=xmin, stop=xmax, step=.1)



#Tanh
def tahn(x):
    y = list(map(lambda x_i: np.tanh(x_i), x))

    plt.figure(figsize = (15,5))
    plt.plot(x,y, linewidth = 4)
    plt.plot([xmin, xmax], [0, 0], linestyle='--', color='#888888')
    plt.title('tanh', fontsize=22)
    plt.show()



#Sigmoid
def sigmoid(x):
    return 1/(1+np.exp(-x))

y = list(map(sigmoid,x))
plt.figure(figsize=(15,5))
plt.plot(x,y, linewidth=4)
plt.title('sigmoid', fontsize=22)
plt.show()



#ReLU
def relu(x):
    if x<0:
        return 0
    if x>=0:
        return x

    y = list(map(relu,x))

    plt.figure(figsize=(15,5))
    plt.plot(x,y, linewidth=4)
    plt.title('relu', fontsize=22)
    plt.show()