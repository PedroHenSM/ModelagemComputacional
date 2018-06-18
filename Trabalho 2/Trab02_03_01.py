#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:46:15 2018
@author: lucasmullers
"""
import numpy as np
import pylab as pl

def funcaoNormal(P,D,d,alfa):
    return (16*P*D*(1 + d/(4*D))*np.sin(alfa))/(np.pi*(d**3))

def funcaoCisalhante(P,D,d,alfa):
    return (8*P*D*(1 + d/(2*D))*np.cos(alfa))/(np.pi*(d**3))

def deslocamento(P,D,d,alfa,E,G,n):
    #return ((8*P*(D**3)*n)/((d**4)*np.cos(alfa))) * (2*((1+(d**2)/(4*(D**2)))*np.sin(alfa)*np.sin(alfa)/E)+(1+(d**2)/(2*(D**2)))*np.cos(alfa)*np.cos(alfa)/E*G)

    term1 = (8*P*np.power(D,3)*n)/(np.power(d,4)*np.cos(alfa))
    term2 = (1+(np.power(d,2)/(4*np.power(D,2)))) * (np.power(np.sin(alfa),2) / E)
    term3 = (1+(np.power(d,2)/(2*np.power(D,2)))) * (np.power(np.cos(alfa),2) / E*G)
    
    return term1 * (2 * term2 + term3)
    

tensaoNormal = []
tensaoCisalhante = []
coefRigidez = [] # F = kx --> k = F/x


for i in range (10000):
    #np.random.seed(i)
    D = np.random.uniform(77,83) * (10**(-3))
    d = np.random.uniform(19,21) * (10**(-3))
    alfa = np.deg2rad(np.random.uniform(13,17))
    n = 10
    E = np.random.uniform(197,203) * (10**(9))
    G = np.random.uniform(79,81) * (10**(9))
    P = 12*10**3
    tensaoNormal.append(funcaoNormal(P,D,d,alfa))
    tensaoCisalhante.append(funcaoCisalhante(P,D,d,alfa))
    coefRigidez.append(P / deslocamento(P,D,d,alfa,E,G,n))
    


#fig = pl.figure(1, figsize=(9, 6))
#ax = fig.add_subplot(111)

pl.hist(tensaoNormal,color = 'blue',edgecolor='black', linewidth=1,bins = 50)
pl.title("Histograma da Tensao Normal")
pl.xlabel ("Valor da tensão Normal (N)")
pl.ylabel("Frequência")
pl.figure()

pl.hist(tensaoCisalhante,color = 'blue',edgecolor='black', linewidth=1,bins = 50)
pl.title("Histograma da Tensão Cisalhante")
pl.xlabel ("Valor da tensão Cisalhante (N)")
pl.ylabel("Frequência")
pl.figure()

pl.hist(coefRigidez,color = 'blue',edgecolor='black', linewidth=1,bins = 50)
pl.title("Histograma do Coeficiente de Rigidez")
pl.xlabel ("Valor do Coeficiente de Rigidez (N)")
pl.ylabel("Frequência")
pl.figure()


dados = []
dados.append(tensaoNormal)
dados.append(tensaoCisalhante)

boxprops = dict(linestyle='-',linewidth=2,color='blue')
medianprops = dict(linestyle='-',linewidth=2,color='red')
meanprops=dict(marker='+', markerfacecolor='black', markeredgecolor='black')


#bp0 = pl.boxplot(dados,1,patch_artist = False,showmeans=True)
bp0 = pl.boxplot(dados,showmeans=True,meanprops=meanprops,boxprops=boxprops,medianprops=medianprops)
pl.xticks([1,2],['Tensão Normal', 'Tensão Cisalhante'])
pl.show()
pl.figure()

bp0 = pl.boxplot(coefRigidez,showmeans=True,meanprops=meanprops,boxprops=boxprops,medianprops=medianprops)
pl.xticks([1],['Coeficiente de Rigidez'])




