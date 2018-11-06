# Jessica Trawick,Gage Kizzar,Monica Hiemer
# 2300326
# trawick@chapman.edu

import numpy as np
import matplotlib as plt

def gradient(a,b,n):
    D=np.zeros((n,n))
    x = np.linspace(a,b,n)
    dx = (b-a)/(n-1)
    ones = np.ones(len(D)-1)
    np.fill_diagonal(D[1:],-ones)
    np.fill_diagonal(D[:,:1],ones)
    D[0][0]=-2
    D[0][1]= 2
    D[n-1][n-1]=2
    D[n-1][n-2]=-2

    D= (1/(2*dx) * D)
    return D

def derivative(func, a, b, n=100):
    vecFunc = np.vectorize(func)
    Df = gradient(a,b,n) @ vecFunc
    return Df

def plot(f,a,b,n=100):
    x = derivative(f,a,b,n=100)
    plt.plot(x)

