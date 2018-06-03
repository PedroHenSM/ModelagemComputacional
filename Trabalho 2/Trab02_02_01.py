#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:05:37 2018

@author: lucasmullers
"""

from numpy import random
import numpy as np

#Cálculo de volume entre dois sólidos usando Monte Carlo

def solidoA(x,y):    
    return 8 - x**2 - y**2
def solidoB(x,y):
    return x**2 + 3*y**2


interno = 0
iteracoes = 1000000
for i in range(iteracoes):
    x = random.rand()*np.sqrt(8)
    y = random.rand()*np.sqrt(8/3)
    z = random.rand()*8

    if z <= solidoA(x,y) and z <= solidoB(x,y):
        interno+=1.  
       
volume = 4.*8.*np.sqrt(8.)*np.sqrt(8./3.)*(interno/iteracoes)

print("Volume = " + str(volume))