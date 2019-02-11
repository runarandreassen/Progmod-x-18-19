# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:30:58 2019

@author: anru0906
"""

# importere biblioteker
from pylab import *

# definere konstanter og startbetingelser
k = 4.84e-2 # ratekonstanten
H0 = 1.0    # startkonsentrasjon av hydrogen i mol/L
I0 = 1.0    # startkonsentrasjon av iod i mol/L
HI0 = 0.0   # startkonsentrasjon av HI i mol/L

# tid
tid = 200
N = 100000
dt = tid/(N-1)


# lage matriser
t = zeros(N)
HI = zeros(N)
H = I = zeros(N)

# definere funksjoner
def HIder(H):
    return k*H**2


# initialbetingelser
HI[0] = HI0
H[0] = H0

# Eulers metode
for i in range(N-1):
    endring = HIder(H[i])
    HI[i+1] = HI[i] + endring*dt
    H[i+1] =  H[i] - 0.5*endring*dt
    t[i+1] = t[i] + dt

# Plotting
legend('Reaksjonshastighet for HI og H')
xlabel('Tid [s]')
ylabel('Konsentrasjon [mol/L]')
plot(t, HI, label='HI')
plot(t, H, label='H eller I')
legend(loc=0)
show()







