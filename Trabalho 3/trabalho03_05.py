#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:14:44 2018

@author: pedrohen
"""

import numpy as np
import matplotlib.pyplot as pl
import string
import operator


np.random.seed(1)
r = 1 # Quantidade inicial de letras no inicio da urna
numEventos = 10000



N = [5,10,20,25] # Numeros de letras
K = [2,5,10,15] # Numero de copias

# Preenche urna U com o numero 'r' de cada letra
for a in range(len(N)):
    for b in range (len(K)):
        numLetras = N[a] # Cores serão representadas por letras
        letras = [string.ascii_uppercase[i] for i in range(numLetras)]
        k = K[b] # Numero de copias da bola que será retirada
        U1 = [] # Urna 1
        U2 = [] # Urna 2
        iguais = 0
        for i in range(numLetras):
            l = letras[i]
            U1 += [l]*r
            U2 += [l]*r 
               
        
        for i in range(numEventos):
            idxEscolhido1 = np.random.choice(len(U1))
            idxEscolhido2 = np.random.choice(len(U2))
            letraEscolhida1 = U1[idxEscolhido1]
            letraEscolhida2 = U2[idxEscolhido2]
            if (letraEscolhida1 == letraEscolhida2): # Letras iguais, cada urna recebe k bolas
                U1 += U1[idxEscolhido1]*k
                U2 += U2[idxEscolhido2]*k
                iguais = iguais + 1
            else: # Letras diferentes
                U1 += U2[idxEscolhido2] # Bola da urna 2 inserida na urna 1
                U2 += U1[idxEscolhido1] # Bola da urna 1 inserida na urna 2
                U1.remove(letraEscolhida1) # Remove bola da urna 1
                U2.remove(letraEscolhida2) # Remove bola da urna 2
                
        # Urna 1
        tipoLetra1,qtd1 = np.unique(U1, return_counts = True)
        L1 = dict(zip(tipoLetra1,qtd1)) # Dicionário com letras e quantidade
        z1 = 1.0*qtd1/len(U1) # Vetor com a porcentagem de cada letra ao fim da urna
        arg1 = np.argsort(z1)
        arg1 = arg1[::-1] # Inverte a ordem do vetor arg
        print(sorted(L1.items(), key=operator.itemgetter(1),reverse=True)) # Imprime dicionario
        
        # Urna 2
        tipoLetra2,qtd2 = np.unique(U2, return_counts = True)
        L2 = dict(zip(tipoLetra2,qtd2)) # Dicionário com letras e quantidade
        z2 = 1.0*qtd2/len(U2) # Vetor com a porcentagem de cada letra ao fim da urna
        arg2 = np.argsort(z2) 
        arg2 = arg2[::-1] # Inverte a ordem do vetor arg
        print(sorted(L2.items(), key=operator.itemgetter(1),reverse=True)) # Imprime dicionario
        
        x1 = np.array(range(len(z1)))
        pl.bar(tipoLetra1[arg1],z1[arg1])
        pl.xticks(x1,tipoLetra1[arg1]) # Coloca as letras no eixo X (o nome)
        pl.title("Porcentagem de letras da urna 1 ao fim do experimento: N: {} k:{}".format(numLetras,k))
        pl.xlabel('Letras')
        pl.ylabel('Frequência')
        pl.show()
        pl.figure()
        
        x2 = np.array(range(len(z2)))
        pl.bar(tipoLetra2[arg2],z2[arg2])
        pl.xticks(x2,tipoLetra2[arg2]) # Coloca as letras no eixo X (o nome)
        pl.title("Porcentagem de letras da urna 2 ao fim do experimento: N: {} k:{}".format(numLetras,k))
        pl.xlabel('Letras')
        pl.ylabel('Frequência')
        pl.show()