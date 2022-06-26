import math
import numpy as np


def make_zeros_matrix(a,b):
    matrix = [([0]*b) for i in range(a)]
    return matrix


def trap(f,n,a,b):
    h = (b-a) / n
    sum = 0
    for i in range(1,n):
        sum = sum + 2 * f(a+i*h)
    Trap = (h/2) * (f(a) + sum + f(b))
    return Trap


def romberg(f,n,a,b):
    i_mtrx = make_zeros_matrix(10,10)
    ea = 100
    n = 1
    i = 1
    i_mtrx[1][1] = trap(f,n,a,b)
    print('Application \t ea \t\t et \t\t Integral')
    while ea > 0.000001:
        n = 2 ** i
        i_mtrx[i+1][1] = trap(f,n,a,b)
        for k in range(2,i+2):
            j = 2 + i - k
            i_mtrx[j][k] = (4**(k-1)*i_mtrx[j+1][k-1] - i_mtrx[j][k-1]) / (4**(k-1)-1)
        ea = abs((i_mtrx[1][i+1] - i_mtrx[2][i]) / i_mtrx[1][i+1]) * 100
        et = abs((1.71828 - i_mtrx[1][i+1]) / 1.7182) * 100
        print('%f\t%f\t%f\t%f'%(i,ea,et,i_mtrx[1][i+1]))
        i+=1

func = lambda x:math.exp(x)

func3 = lambda x: math.sin(x)


romberg(func3,1,0,math.pi)







