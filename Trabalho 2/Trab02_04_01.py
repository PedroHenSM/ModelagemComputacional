#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:11:15 2018

@author: lucasmullers
"""

import numpy as np

def omega(G,h,Eo,to,Ei,ti):
    return np.square(G/h * (1/(Eo*to) + 2/(Ei*ti)))

def tensaoCisalhamento(P,omega,b,x,Eo,to,Ei,ti,alfao,alfai,T,l):
    primeiroTermo = (P*omega*np.cosh(omega*x))/(4*b*np.sinh(omega*l/2))
    segundoTermo = (P*omega*((2*Eo*to - Ei*ti)/(2*Eo*to + Ei*ti)))/(4*b*np.cosh(omega*l/2))
    terceiroTermo =  ((alfai - alfao)*T*omega)/((1/(Eo*to) + 2/(Ei*ti))*np.cosh(omega*l/2))
    
    return primeiroTermo + (segundoTermo + terceiroTermo)*np.sinh(omega*x)

G = np.random.uniform(0.2 *(10**6)*0.95, 0.2 *(10**6)*1.05)
Eo = np.random.uniform(10*(10**6)*0.95, 10*(10**6)*1.05)
Ei = np.random.uniform(30*(10**6)*0.95, 30*(10**6)*1.05)
alfao = np.random.uniform(6*(10**-6)*0.95, 6*(10**-6)*1.05)
alfai = np.random.uniform(13*(10**-6)*0.95, 13*(10**-6)*1.05)
h = np.random.uniform(0.020*0.95, 0.020*1.05)
l = np.random.uniform(0.95, 1.05)
b = np.random.uniform(0.95,1.05)
T = np.random.uniform(70*0.95, 70*1.05) - np.random.uniform(200*.095, 200*1.05)
to = np.random.uniform(0.15*0.95, 0.15*1.05)
ti = np.random.uniform(0.1*0.95, 0.1*1.05)
P = np.random.uniform(2000*0.95, 2000*1.05)
