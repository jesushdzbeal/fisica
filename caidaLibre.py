#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 18:13:55 2021

@author: dr.guillermo
"""
import numpy as np
import matplotlib.pyplot as plt

g= 9.8  # gravedad
m= 68.1 # masa
cd=12.5 #coeficiente de resistencia, factor ropa
tf=2    # tiempo final

# ecuación de la caida libre
v= g*m/cd*(1-np.exp(-cd/m*tf))

#imprimir el resultado v 
print("Vel Final=")
print(v)
#x=np.array() 
#y=np.array()
# genero 2 vectores y los llleno de ceros
N=100
x = np.zeros(N)
y = np.zeros(N)

#x=np.linspace(min(x),max(x),100)
# llenar a x con valores sucesivvos del 0 al 100
x= np.arange(0,N)
# evaluar la función en cada x
# el for va desde 0 a 100
for i in range(N):
     y[i] =g*m/cd*(1-np.exp(-cd/m*x[i]))

# grafica de x,y, rayas azules
plt.plot(x,y,'b-')
plt.title('Caida Libre')
plt.xlabel('Tiempo')
plt.ylabel('Velocidad')
plt.show()