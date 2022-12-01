from math import sqrt

def f(a,b):

    eps = 10e-7

    while abs(a - b) > eps:
        a, b = sqrt(a*b), (a+b)/2

    print(a)

f(10,20)