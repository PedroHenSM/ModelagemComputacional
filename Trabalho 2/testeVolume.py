#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:15:31 2018

@author: lucasmullers
"""

#https://www.tutorbrasil.com.br/forum/viewtopic.php?t=36000

import numpy as np

def solidoA(x,y):    
    return 8 - x**2 - y**2
def solidoB(x,y):
    return x**2 + y**2


interno = 0
iteracoes = 1000000
for i in range(iteracoes):
    x = np.random.uniform(0, 8)
    y = np.random.uniform(0, 8)
    z = np.random.uniform(0, 8)

    if z <= solidoA(x,y) and z <= solidoB(x,y):
        interno+=1.   
       
volume = 4.*8.*8.*8.*(interno/iteracoes)

print("Volume = " + str(volume))