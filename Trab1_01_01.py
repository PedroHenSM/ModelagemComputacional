#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:09:15 2018

@author: pedrohen
"""

import numpy as np
import pylab as pl

def f(r,k):
    return  r + r*k*(1500-r)

#k  = 0.0012
k =  0.0025
r = 4

r_vec = []
dias_vec = []
numDias = 0 
while r < 1500:
    r_vec.append(f(r,k))
    #r = f(r,k)
    dias_vec.append(numDias)
    numDias = numDias + 1

#r_vec.append(r)
#dias_vec.append(numDias)
    #r = f(r,k)
pl.plot(dias_vec,r_vec,'-' 'o',label = "Grafico 1")
xlim(0,1500)
pl.grid()
pl.xlabel("Tempo (dias)")
pl.ylabel("Boatos (pessoas que sabem)")
pl.legend()
pl.show()




