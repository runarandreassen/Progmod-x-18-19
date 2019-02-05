# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:19:19 2019

@author: anru0906
"""

# importere bibliotek
from pylab import *

# definere konstanter
k = 0.1
H0 = 1000

# tidsintervaller
t = 120
N = 100000
dt = t/(N-1)


# definere funksjoner
def Hder(t, H):
    return k*H

# lage matriser
t = zeros(N)
H = zeros(N)

# definere initialbetingelser
t[0] = 0.0
H[0] = H0

# Eulers metode
for i in range(N-1):
    H[i+1] = H[i]+Hder(t[i], H[i])*dt
    t[i+1] = t[i] + dt

# Lage plot
plot(t, H)
title('Antall harer på øde øy')
xlabel('Tid i måneder')
ylabel('Antall harer')










 






   





