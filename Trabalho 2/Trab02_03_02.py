#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:46:15 2018
@author: lucasmullers
"""
import numpy as np
import pylab as pl

def funcaoNormal(P,D,d,alfa):
    return (16*P*D*(1 + d/(4*D))*np.sin(alfa))/(np.pi*d**3)

def funcaoCisalhante(P,D,d,alfa):
    return (8*P*D*(1 + d/(2*D))*np.cos(alfa))/(np.pi*d**3)

def deslocamento(P,D,d,alfa,E,G,n):
    #return ((8*P*(D**3)*n)/((d**4)*np.cos(alfa))) * (2*((1+(d**2)/(4*(D**2)))*np.sin(alfa)*np.sin(alfa)/E)+(1+(d**2)/(2*(D**2)))*np.cos(alfa)*np.cos(alfa)/E*G)

    term1 = (8*P*np.power(D,3)*n)/(np.power(d,4)*np.cos(alfa))
    term2 = (1+(np.power(d,2)/(4*np.power(D,2)))) * (np.power(np.sin(alfa),2) / E)
    term3 = (1+(np.power(d,2)/(2*np.power(D,2)))) * (np.power(np.cos(alfa),2) / E*G)
    
    return term1 * (2 * term2 + term3)
    
def calculaTensaoLimite(normal,cisalhante):
    return np.sqrt(np.power(normal,2)+4*np.power(cisalhante,2))

tensaoNormal = []
tensaoCisalhante = []
tensaoLimite = []
falhou = 0
numVezes = 10000

for i in range (numVezes):
    #np.random.seed(i)
    D = np.random.uniform(77,83) * (10**(-3))
    d = np.random.uniform(19,21) * (10**(-3))
    alfa = np.random.uniform(13,17)
    n = 10
    E = np.random.uniform(197,203) * (10**(9))
    G = np.random.uniform(79,81) * (10**(9))
    P = 10.2*10**3
    tensaoNormal.append(funcaoNormal(P,D,d,alfa))
    tensaoCisalhante.append(funcaoCisalhante(P,D,d,alfa))
    tensaoLimite.append(calculaTensaoLimite(tensaoNormal[i],tensaoCisalhante[i]))
    if (tensaoLimite[i] > 600 * 10**6):
        falhou = falhou + 1
        
pl.hist(tensaoLimite,color = 'blue',edgecolor='black', linewidth=1,bins = 50)
pl.title("Histograma da Tensao Limite")
pl.axvline(x = 600 * 10**6,color = 'red',linestyle = 'dashed')
pl.xlabel ("Valor da tensão Limite (N)")
pl.ylabel("Frequência")
pl.figure()

legendas = ["Falhou","Resistiu"]
pedacos = [falhou,numVezes-falhou]
cores = ['red','lightskyblue']
explode = (0.1,0)
pl.pie(pedacos,explode = explode,colors=cores,autopct='%1.1f%%',shadow = True, startangle = 0) #'''startangle = 90''')
pl.title("Eficiência da Mola")
pl.axis('equal')
pl.legend(legendas,loc = 'best')
pl.show()

        

        
    





