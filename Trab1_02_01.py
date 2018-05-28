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
estacionario = 0
man.append(ma)
mbn.append(mb)
men.append(me)
index.append(0)
for i in range(30):
    man.append(0.900*ma + 0.15*mb + 0.25*me)
    mbn.append(0.075*ma + 0.80*mb + 0.25*me)
    men.append(0.025*ma + 0.05*mb + 0.50*me)
    index.append(i+1)
    print("Ma-Man= {}".format(abs(ma-man[i+1])))
    if ( estacionario == 0 and abs(ma - man[i+1]) < 1 and abs(mb - mbn[i+1]) < 1 and abs(me - men[i+1]) < 1):
        estacionario = index[i]
    ma = man[i+1]
    mb = mbn[i+1]
    me = men[i+1]

print("MA:{}\tMB:{}\tME:{}".format(ma,mb,me))
pl.plot(index, man, 'o''-',label="Mercado em alta")
pl.plot(index, mbn, 'o''-',label="Mercado em baixa")
pl.plot(index, men, 'o''-',label="Mercado estagnado")
pl.axvline(x=estacionario,linestyle = '--',color = 'red')
pl.xlabel("Tempo(semanas)")
pl.ylabel("Empresas em cada mercado")
pl.title("Mercados ao longo da semana")
pl.grid()
pl.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0)
pl.show()
    