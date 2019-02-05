# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:26:10 2019

@author: anru0906
"""

# Importere biblioteker
from pylab import *

# Definere konstanter
g = 9.81    #tyngdens akselerasjon i m/s^2
m = 2.0    # Vekt av kule
k = 0.2

# Tidsintervall
N = 100000
t = 2.0    # Total tid vi observerer kula
dt = t/(N-1)


# Lage matriser
t = zeros(N)
s = zeros(N)
v = zeros(N)
a = zeros(N)

# Definere initialbetingelser
t[0] = 0.0
s[0] = 0.0
v[0] = 0.0

# Definere funksjoner
def a1(t, v):
    return g - k/m*v**2


# Eulers metode
for i in range(N-1):
    a[i] = a1(t[i], v[i])
    v[i+1] = v[i] + a[i]*dt
    s[i+1] = s[i] + v[i]*dt
    t[i+1] = t[i] + dt

# Plotte data
subplot(3, 1, 1)
plot(t, s, '-b')
title('Posisjonsgraf')
xlabel('Tid [s]')
ylabel('Posisjon [m]')

subplot(3, 1, 2)
plot(t, v, '-r')
title('Fartsgraf')
xlabel('Tid [s]')
ylabel('Fart [m/s]')

subplot(3, 1, 3)
plot(t, a, '-g')
title('Akselerasjonsgraf')
xlabel('Tid [s]')
ylabel('Akselerasjon [m/s^2]')

subplots_adjust(top=3.4, bottom=1.0, left=0.1, right = 1.0,
               hspace=0.4, wspace=0.4)
show()








    
   






 
    
    
    
    
    
