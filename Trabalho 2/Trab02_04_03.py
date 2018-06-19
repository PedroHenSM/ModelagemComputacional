#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:11:15 2018

@author: lucasmullers
"""

import numpy as np
import pylab as pl

def omega(G,h,Eo,to,Ei,ti):
    return np.sqrt(G/h * (1/(Eo*to) + 2/(Ei*ti)))

def tensaoCisalhamento(P,omega,b,x,Eo,to,Ei,ti,alfao,alfai,T,l):
    primeiroTermo = (P*omega*np.cosh(np.deg2rad(omega*x)))/(4*b*np.sinh(np.deg2rad(omega*l/2)))
    segundoTermo = (P*omega*((2*Eo*to - Ei*ti)/(2*Eo*to + Ei*ti)))/(4*b*np.cosh(np.deg2rad(omega*l/2)))
    terceiroTermo =  ((alfai - alfao)*T*omega)/((1/(Eo*to) + 2/(Ei*ti))*np.cosh(np.deg2rad(omega*l/2)))
    
    return primeiroTermo + (segundoTermo + terceiroTermo)*np.sinh(np.deg2rad(omega*x))


minimo = 1000000
maximo = 0
vetor = []
for j in range(80):
    G = np.random.uniform(0.2 *(10**6)*0.95, 0.2 *(10**6)*1.05)
    Eo = np.random.uniform(10*(10**6)*0.95, 10*(10**6)*1.05)
    Ei = np.random.uniform(30*(10**6)*0.95, 30*(10**6)*1.05)
    alfao = np.random.uniform(13*(10**-6)*0.95, 13*(10**-6)*1.05)
    alfai = np.random.uniform(6*(10**-6)*0.95, 6*(10**-6)*1.05)
    h = np.random.uniform(0.020*0.95, 0.020*1.05)
    l = np.random.uniform(0.95, 1.05)
    b = np.random.uniform(0.95,1.05)
    T = np.random.uniform(70*0.95, 70*1.05) - np.random.uniform(200*.095, 200*1.05)
    to = np.random.uniform(0.15*0.95, 0.15*1.05)
    ti = np.random.uniform(0.1*0.95, 0.1*1.05)
    P = np.random.uniform(2000*0.95, 2000*1.05)
    omegaVal = omega(G,h,Eo,to,Ei,ti)
    x = np.linspace(0,0.5,50)
    tensoes = []
    
    for xi in x:
        tensoes.append(tensaoCisalhamento(P,omegaVal,b,xi,Eo,to,Ei,ti,alfao,alfai,T,l))
    vetor.append(tensoes)
    if min(tensoes) < minimo:
        minimo = min(tensoes)
    if max(tensoes) > maximo:
        maximo = max(tensoes)
    pl.plot(x,tensoes)
    pl.grid()
    pl.title("Tensão cisalhante por distância")
    pl.xlabel("Distância (in)")
    pl.ylabel("Tensão cisalhante (lbf/in²)")
pl.show()
pl.figure()
pl.boxplot(vetor)
print("valor mínimo:" + str(minimo) + "\nvalor máximo: " + str(maximo))
