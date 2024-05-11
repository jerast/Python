from math import *
import numpy as numpy
import matplotlib.pyplot as pyplot

def f(x):
     return numpy.cos(x) - x**2

def bisection(x1, x2, err):
     a = x1
     b = x2
     counter = 0

     if f(a) * f(b) > 0:
          return 'El intervalo no sirve'

     while ( abs(a-b) > err ):
          xr = (b + a) / 2
          if f(a) * f(xr) < 0:
               b = xr
          if f(b) * f(xr) < 0:
               a = xr
          counter += 1
          print(f'{counter} - [ {a}, {b} ]')
          
     print('\n', f'xr = {xr} es la mejor aprox.')
     
def graphic():
     x = numpy.linspace( pi/9, pi/3, 1000 )
     pyplot.plot(x, f(x))
     pyplot.xlabel('X')
     pyplot.ylabel('Y')
     pyplot.title('f(x) = cos(x) - x^2')
     pyplot.show()

bisection(0, pi/2, 10**-4)
graphic()