# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:01:44 2019

@author: anru0906
"""
#Et program som definerer metoder for integrasjon
def rektangel(f, a, b, n):
    h = (b - a)/n
    sum = 0
    for k in range(0, n):
        sum += f(a + k*h)
    return sum*h

def trapes(f, a, b, n):
    h = (b - a)/n
    sum = (f(a) + f(b))/2.0
    for k in range(1, n):
        sum += f(a + k*h)
    return sum*h

def simpsonsb(f, a, b, n):
    h = (b - a)/n
    sum = f(a) + f(b)
    for k in range(1, n, 2):
        sum += 4*f(a + k*h)
    for k in range(2, n-1, 2):
        sum += 2*f(a + k*h)
    return sum*h/3

def simpsonsr(f, a, b, n):
    h = (b - a)/n
    sum = f(a) + f(b)
    g = int(n/2)
    for k in range(2, g+1):
        sum += 2*f(a + (2*k - 2)*h)
    for k in range(1, g+1):
        sum += 4*f(a + (2*k - 1)*h)
    return sum*h/3
        
        
        
        
        
        
        
        
        
        