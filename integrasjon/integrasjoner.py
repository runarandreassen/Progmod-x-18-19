# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:11:46 2019

@author: anru0906
"""

from integrasjon import *

a = 0
b = 3
n = 1

def f(x):
    return x**2

print('%10s %10s %10s %10s %10s' % ('h', 'rektangel', 'trapes',
                                    'simpsonsb', 'simpsonsr'))
print('_'*57)
for i in range(200):
    print('%10.1e %10.5f %10.5f %10.5f %10.5f' % (n, rektangel(f, a, b, n),
                                                  trapes(f, a, b, n),
                                                  simpsonsb(f, a, b, n),
                                                  simpsonsr(f, a, b, n)))
    n += 1
'''print(rektangel(f, a, b, n))
print(trapes(f, a, b, n))
print(simpsonsb(f, a, b, n))
print(simpsonsr(f, a, b, n))'''