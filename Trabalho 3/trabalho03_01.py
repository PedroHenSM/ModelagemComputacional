#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 19:20:07 2018

@author: pedrohen
"""

# N = Numero de cores (letras)
# k = Numero de bolas que serão colocadas na urna após retirar, além da retirada

import numpy as np
import matplotlib.pyplot as pl
import string

np.random.seed()
r = 1 # Quantidade inicial de letras no inicio da urna
numEventos = 10000

renda = {}


N = [5,10,20,25] # Numeros de letras
K = [2,5,10,15] # Numero de copias

# Preenche urna U com o numero 'r' de cada letra
for a in range(len(N)):
    for b in range (len(K)):
        numLetras = N[a] # Cores serão representadas por letras
        letras = [string.ascii_uppercase[i] for i in range(numLetras)]
        k = K[b] # Numero de copias da bola que será retirada
        U = [] # Urna
        for i in range(numLetras):
            #l = letras[nLetras-i-1]
            l = letras[i]
            U += [l]*r
            #renda[l] = (i+1)
               

        
        for i in range(numEventos):
            idxEscolhido = np.random.choice(len(U))
            U += U[idxEscolhido]*k
            
            
        tipoLetra,qtd = np.unique(U, return_counts = True)
        L = dict(zip(tipoLetra,qtd)) # Dicionário com letras e quantidade
        print(L)
        print(len(U))
        z = 1.0*qtd/len(U) # Vetor com a porcentagem de cada letra ao fim da urna
        arg = np.argsort(z) # Returns the indices that would sort an array.
        arg = arg[::-1] # Inverte a ordem do vetor arg
        
        
        x = np.array(range(len(z)))
        pl.bar(tipoLetra,z)
        #pl.bar(x,z[arg]) # ?????
        pl.xticks(x,tipoLetra) # Coloca as letras no eixo X ( o nome) | Apenas estética
        pl.title("Porcentagem de letras ao fim do experimento: N: {} k:{}".format(numLetras,k))
        pl.xlabel('Letras')
        pl.ylabel('Frequência')
        pl.show()





##pl.semilogx(x,z, tipoLetras='r', lw=3)
##pl.show()
#
#cc=np.polyfit(x=x, y=np.log(z[arg]), deg=1); p=np.poly1d(cc)
#pl.plot(x,np.log(z[arg]),'r', x,p(x), 'b')
#pl.show()
#
#print(p)
