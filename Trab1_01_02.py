#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:16:21 2018

@author: pedrohen
"""

import numpy as np
import pylab as pl

def f(r,k):
    return r + r*k*(5500-r)

k = [0.25, 0.025, 0.0025, 0.00025]
r = 4




for i in range(4): # Tamanho de k 
    r_vec = []
    dias_vec = []
    r = 4
    for numDias in range(1,8): # Uma semana
        r = f(r,k[i])
        r_vec.append(r)
        dias_vec.append(numDias)
    pl.plot(dias_vec,r_vec,'-' 'o',label = "Grafico {}".format(i+1))
    pl.grid()
    
    pl.xlabel("Tempo (dias)")
    pl.ylabel("Boatos (pessoas que sabem)")
    pl.legend()
    pl.show()
    pl.figure()    



#pl.show()
