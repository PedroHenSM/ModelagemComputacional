#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:46:15 2018

@author: lucasmullers
"""
import numpy as np

def funcaoNormal(P,D,d,alfa):
    return (16*P*D*(1 + d/(4*D))*np.sin(alfa))/(np.pi*d**3)

def funcaoCisalhante(P,D,d,alfa):
    return (8*P*D*(1 + d/(2*D))*np.cos(alfa))/(np.pi*d**3)

D = np.random.uniform(77,83) * (10**(-3))
d = np.random.uniform(19,21) * (10**(-3))
alfa = np.random.uniform(13,17)
n = 10
E = np.random.uniform(197,203) * (10**(9))
G = np.random.uniform(79,81) * (10**(9))
P = 12*10**3

