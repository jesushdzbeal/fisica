#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:55:23 2021

@author: dr.guillermo
"""
# importamos librerias, clases 
import numpy as np
import matplotlib.pyplot as plt

#tiempo
t = np.array([0,10, 20, 30, 40, 50]) 
#posición
x = np.array([0,50,100,150, 200,250])

print(t)
print(x)
# Gráficamos los datos experimentales
plt.plot(t,x,'ro')

deltax= x[5]- x[0]
print("dx= ")
print(deltax)

deltat= t[5]- t[0]
print("dt= ")
print(deltat)

vxprom= deltax/deltat
print("Vxprom= ")
print(vxprom)

#xx = np.linspace(0,50,100)
#yy = 
plt.plot(t, x, 'o--', color='blue', label='A-F', alpha=0.3)

plt.grid(axis='both', color='0.95')
plt.legend(title='Posición')
plt.title('Trayectoria de la Particula')
plt.show()
