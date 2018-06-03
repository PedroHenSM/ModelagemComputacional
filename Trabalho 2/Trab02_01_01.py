#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:00:19 2018

@author: lucasmullers
"""

from numpy import random
import pylab as pl

def equacaoCirculo(x,y):
    return x**2 + y**2

dentroDoCirculo = 0
iteracoes = 10000
x_interno = []
x_externo = []
y_interno = []
y_externo = []

for i in range(iteracoes):
    x = random.rand()
    y = random.rand()
    
    if equacaoCirculo(x,y) <= 1.0:
        dentroDoCirculo +=1
        x_interno.append(x)
        y_interno.append(y)
    else:
        x_externo.append(x)
        y_externo.append(y)
        
pl.scatter(x_interno, y_interno, c='blue')
pl.scatter(x_externo, y_externo, c='red')
pl.axvline(x=1, linestyle='--', color='black')
pl.axhline(y=1, linestyle='--', color='black')
pl.show()

pi = 4 * dentroDoCirculo / iteracoes
print("O valor de pi eh: " + str(pi))