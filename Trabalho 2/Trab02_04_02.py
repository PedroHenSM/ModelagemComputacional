#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:34:43 2018

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


G = 0.2*(10**6)
Eo = 10*(10**6)
Ei = 30*(10**6)
alfao = 13*(10**-6)
alfai = 6*(10**-6)
h = 0.020
l = 1
b = 1
T = 70 - 200
to = 0.15
ti = 0.1
P = 2000
omegaVal = omega(G,h,Eo,to,Ei,ti)
x = np.linspace(0,0.5,50)
tensoes = []

for xi in x:
    tensoes.append(tensaoCisalhamento(P,omegaVal,b,xi,Eo,to,Ei,ti,alfao,alfai,T,l))
pl.plot(x,tensoes)
pl.grid()
pl.title("Tensão cisalhante por distância")
pl.xlabel("Distância (in)")
pl.ylabel("Tensão cisalhante (Pa)")
pl.show()