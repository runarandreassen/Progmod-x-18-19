# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 15:18:11 2019

@author: anru0906
"""

# Importerer bibliotek
from pylab import *

# Definere konstanter
a = 0.1     # Reproduksjonsraten
b = 10000   # Bæreevne
c = 0.005   # hvor mange harer som møter gaupe og blir spist
d = 0.00005 # gaupevekst pr hare spist
e = 0.06    # nedgangsrate hos gauper
H0 = 2000
G0 = 10

# Tidsintervall
t = 400     # antall måneder forsøket varer
N = 100000
dt = t/(N-1)

# Definere funksjoner
def Hder(t, H, G):
    return a*H*(1 - H/b) - c*H*G
def Gder(t, H, G):
    return d*H*G - e*G

# Lage matriser
t = zeros(N)
H = zeros(N)
G = zeros(N)

# Initialbetingelser
t[0] = 0
H[0] = H0
G[0] = G0

# Eulers metode
for i in range(N-1):
    Hder(t[i], H[i], G[i])
    Gder(t[i], H[i], G[i])
    H[i+1] = H[i] + Hder(t[i], H[i], G[i]) * dt
    G[i+1] = G[i] + Gder(t[i], H[i], G[i]) * dt
    t[i+1] = t[i] + dt

# Lage plot
fig = figure()
ax = fig.add_subplot(111)
data1 = ax.plot(t, H, '-b', label = 'Harer')
ax2 = ax.twinx()
data2 = ax2.plot(t, G, '-r', label = 'Gauper')

data = data1 + data2
datatittel = [l.get_label() for l in data]
ax.legend(data, datatittel, loc=0)

ax.grid()
ax.set_xlabel('Tid [mnd]')
ax.set_ylabel('Antall harer')
ax2.set_ylabel('Antall gauper')
ax2.set_ylim(0, 30)
ax.set_ylim(0, 2500)
plt.show()















