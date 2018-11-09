# Jessica Trawick,Gage Kizzar,Monica Hiemer
# 2300326
# trawick@chapman.edu

import numpy as np
import matplotlib.pyplot as plt

def gradient(a,b,n):
    D=np.zeros((n,n))
    x = np.linspace(a,b,n)
    dx = (b-a)/(n-1)
    ones = np.ones(len(D)-1)
    np.fill_diagonal(D[1:],-ones)
    np.fill_diagonal(D[:, 1:],ones)
    D[0][0]=-2
    D[0][1]= 2
    D[n-1][n-1]=2
    D[n-1][n-2]=-2

    D= (1/(2*dx) * D)
    return D

def f_plot(a, b, n):
    x = np.linspace(a,b,n)
    fx = [i**2 for i in x ]
    Df = gradient(a, b , n)
    f_grad= Df@fx
    plt.plot(x, fx , label = "f(x)")
    plt.plot(x, f_grad , label = "f'(x)")
    plt.legend()
    plt.title("$x^2$ function and the derivative")
    

def f_plot_grad(a,b , n ):
    x = np.linspace(a,b,n)
    fx = [i**2 for i in x ]
    f_grad = np.gradient(fx)
    plt.plot(x, fx , label ="f(x)")
    plt.plot(x, f_grad , label ="f'(x)")
    plt.legend()
    plt.title ("$x^2$ function and the derivative using np.gradient")

def f_second(a,b, n):
    x = np.linspace(a,b,n)
    fx = [i**2 for i in x ]
    D = gradient(a, b , n)
    Df= D@D
    f_grad= D@fx
    f_2_grad= Df@fx
    plt.plot(x, fx , label ="f(x)")
    plt.plot(x, f_grad , label ="f(x)")
    plt.plot(x, f_2_grad, label = "f''(x)")
    plt.legend()
    plt.title ("$x^2$ function and it's first and second derivatives")
    
def s_plot(a, b , n):
    x = np.linspace(a,b,n)
    fx = [np.sin(i) for i in x ]
    Df = gradient(a, b , n)
    f_grad= Df@fx
    plt.plot(x, fx , label ="f(x)")
    plt.plot(x, f_grad , label ="f'(x)")
    plt.legend()
    plt.title ("Sin(x) fucntion and it's derivative")
    
def s_polt_grad(a, b, n ):
    x = np.linspace(a,b,n)
    fx = [np.sin(i) for i in x ]
    Df = np.gradient(fx)
    f_grad = np.gradient(fx)
    plt.plot(x, fx , label ="f(x)")
    plt.plot(x, f_grad , label ="f'(x)")
    plt.legend()
    plt.title ("sin(x) function and it's derivative using np.gradient")
    
def g_plot(a, b , n ):
    x = np.linspace(a,b,n)
    fx = [(np.divide((np.exp(np.divide(-(i**2), 2))), np.sqrt(2*np.pi))) for i in x]
    Df = gradient(a, b , n)
    f_grad= Df@fx
    plt.plot(x, fx , label ="f(x)")
    plt.plot(x, f_grad , label ="f'(x)")
    plt.legend()
    plt.title (" $e^{-x^2/2}/\sqrt{2\pi}$ function and it's derivative")
    
def g_plot_grad(a, b, n):
    x = np.linspace(a, b, n)
    fx = [(np.divide((np.exp(np.divide(-(i**2), 2))), np.sqrt(2*np.pi))) for i in x]
    f_grad = np.gradient(fx)
    plt.plot(x, fx, label = "f(x)")
    plt.plot(x, f_grad, label = "f'(x)")
    plt.legend()
    plt.title(" $e^{-x^2/2}/\sqrt{2\pi}$ function and its derivative using np.gradient")

    
    
    
    
    
    
    
    