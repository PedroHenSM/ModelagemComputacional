#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:11:49 2018

@author: lucasmullers
"""

import pylab as pl

r = [200,300,200,20]
c = [150,150,100,10]
casos = ['A','B','C','D']
fr = 0.125

for i in range(len(casos)):
    tempo = []
    rn = []
    cn = []
    rn.append(r[i])
    cn.append(c[i])
    tempo.append(0)
    for j in range(120):
        rn.append(1.2*r[i] - 0.001*r[i]*c[i] - fr*r[i])
        cn.append(0.7*c[i] + 0.002*r[i]*c[i])
        r[i] = rn[j+1]
        c[i] = cn[j+1]
        tempo.append(j+1)
        
    pl.title("Caso "+str(casos[i]))
    pl.plot(tempo, rn, '-', label="População de ratos")
    pl.plot(tempo, cn, '-', label="População de corujas")
    pl.xlabel("Tempo(Meses)")
    pl.ylabel("Quantidade de ratos/corujas")
    pl.grid()
    pl.legend()
    pl.show()  