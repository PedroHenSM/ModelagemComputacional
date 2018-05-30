#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:28:25 2018

@author: pedrohen/lucasmullers
"""

import pylab as pl

def f(r,k,d): # Funcao que controla a taxa de crescimento do boato 
    return r + r*k*(1500-r) - r*(e*d)

k  = 0.0012
r = 4

e = 0.025

r_vec = []
dias_vec = []
numDias = 0 
for numDias in range(90):
    r = f(r,k,numDias)
    r_vec.append(r)
    dias_vec.append(numDias)

pl.plot(dias_vec,r_vec,'-')
pl.title("Dispersão do boato com fator de esquecimento")
pl.grid()
pl.xlabel("Tempo (dias)")
pl.ylabel("Boatos (pessoas que sabem)")
pl.legend()
pl.show()