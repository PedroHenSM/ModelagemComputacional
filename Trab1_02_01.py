#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:25:14 2018

@author: pedrohen
"""

import pylab as pl

ma = 1000
mb = 1000
me = 2000
man = []
mbn = []
men = []
index = []
for i in range(30):
    man.append(0.900*ma + 0.15*mb + 0.25*me)
    mbn.append(0.075*ma + 0.80*mb + 0.25*me)
    men.append(0.025*ma + 0.05*mb + 0.50*me)
    index.append(i)
    ma = man[i]
    mb = mbn[i]
    me = men[i]
    
pl.plot(index, man, 'o''-',label="Mercado em alta")
pl.plot(index, mbn, 'o''-',label="Mercado em baixa")
pl.plot(index, men, 'o''-',label="Mercado estagnado")
pl.xlabel("Tempo(semanas)")
pl.ylabel("Empresas em cada mercado")
pl.title("Mercados ao longo da semana")
pl.grid()
pl.legend(loc='upper right')
pl.show()
    