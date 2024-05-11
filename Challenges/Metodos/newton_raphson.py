from math import *
import numpy as numpy
import matplotlib.pyplot as pyplot

def f(x):
     return numpy.cos(x) - x**2

def df(x):
    return -sin(x) - 2*x

def newtonRaphston(x0, err, iterations = 10):
     for i in range(1, iterations + 1):
          x1 = x0 - f(x0) / df(x0)
          print(f'{i} - [ {x1} ]')

          if ( abs(x1-x0) < err ):
               break
          
          x0 = x1

     print(f'xr = {x1} es la raíz.')

def graphic():
     x = numpy.linspace( pi/9, pi/3, 1000 )
     pyplot.plot(x, f(x))
     pyplot.xlabel('X')
     pyplot.ylabel('Y')
     pyplot.title('f(x) = cos(x) - x^2')
     pyplot.show()

newtonRaphston(pi, 10**-4)
graphic()