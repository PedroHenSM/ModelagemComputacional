#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:05:37 2018

@author: lucasmullers
"""

import numpy as np

#Cálculo de volume entre dois sólidos usando Monte Carlo

def solidoA(x,y):    
    return 8 - np.power(x,2) - np.power(y,2)
def solidoB(x,y):
    return np.power(x,2) + 3*np.power(y,2)


iteracoes = 1000000
volume = []
for k in range(100):
    interno = 0
    print(k)
    for i in range(iteracoes):
        x = np.random.uniform(0, 8)
        y = np.random.uniform(0, 8)
        z = np.random.uniform(0, 8)
    
        if z <= solidoA(x,y) and z <= solidoB(x,y):
            interno+=1.
           
    volume.append(4.*8.*8.*8.*(interno/iteracoes))
    
print("Volume = " + str(sum(volume)/len(volume)))