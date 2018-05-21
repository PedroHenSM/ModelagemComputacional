#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:24:58 2018

@author: lucasmullers
"""

import pylab as pl

r = [200,300,200,20]
c = [150,150,100,10]
casos = ['A','B','C','D']

for i in range(4):
    tempo = []
    rn = []
    cn = []
    for j in range(12):
        rn.append(1.2*r[i] - 0.001*r[i]*c[i])
        cn.append(0.7*c[i] + 0.002*r[i]*c[i])
        r[i] = rn[j]
        c[i] = cn[j]
        tempo.append(j)
        
    pl.title("Caso "+str(casos[i]))
    pl.plot(tempo, rn, '-', label="População de ratos")
    pl.plot(tempo, cn, '-', label="População de corujas")
    pl.xlabel("Tempo(Meses)")
    pl.ylabel("Variação ratos/corujas")
    pl.grid()
    pl.legend()
    pl.show()   