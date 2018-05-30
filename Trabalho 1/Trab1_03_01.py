#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:36:02 2018

@author: pedrohen/lucasmullers
"""

import pylab as pl

p = [100,200,100,100]
q = [500,500,600,400]
tempo = []
pn = []
qn = []
casos = ['A','B','C','D']

for i in range(4):
    tempo = []
    pn = []
    qn = []
    pl.figure()
    pn.append(p[i])
    qn.append(q[i])
    tempo.append(0)
    for j in range(50):
        pn.append(p[i] - 0.1*(q[i] - 500))
        qn.append(q[i] + 0.2*(p[i] - 100))
        tempo.append(j+1)
        p[i] = pn[j+1]
        q[i] = qn[j+1]
        
    pl.title("Caso "+str(casos[i]))
    pl.plot(tempo, pn, '-', label="Preco Produto")
    pl.plot(tempo, qn, '-', label="Quantidade")
    pl.xlabel("Tempo(Meses)")
    pl.ylabel("Variação oferta/preço")
    pl.grid()
    pl.legend()
    pl.show()        
