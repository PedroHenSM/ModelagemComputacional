#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:09:15 2018

@author: pedrohen/lucasmullers
"""

import numpy as np
import pylab as pl

def f(r,k):
    return  r + r*k*(1500-r)

k  = 0.0012
r = 4

r_vec = []
dias_vec = []
numDias = 0 
while r < 1500:
    r = f(r,k)
    r_vec.append(r)
    #r = f(r,k)
    dias_vec.append(numDias)
    numDias = numDias + 1

pl.plot(dias_vec,r_vec,'-' 'o',label = "Grafico 1")
pl.grid()
pl.xlabel("Tempo (dias)")
pl.ylabel("Boatos (pessoas que sabem)")
pl.legend()
pl.show()




