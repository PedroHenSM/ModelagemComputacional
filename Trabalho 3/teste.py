import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
import string
# Modelo para estudar
# http://netlogoweb.org/launch#http://netlogoweb.org/assets/modelslib/Curricular%20Models/Urban%20Suite/Urban%20Suite%20-%20Economic%20Disparity.nlogo
# discussão
# http://www.bbc.com/portuguese/brasil-44205520

# Para leitura:
#
#http://klein.sbm.org.br/wp-content/uploads/sites/17/2016/02/Zipt-bortolossi-queiroz-dasilva-lpp-projeto-klein.pdf
#https://www.revistas.usp.br/ee/article/viewFile/35858/38574
#http://www.periodicos.ufpb.br/index.php/economia/article/view/18844

# Lei 80/20 de Pareto
# https://www.manufaturaemfoco.com.br/ferramentas-de-apoio-gestao-de-operacoes-principio-de-pareto/


# Inovação
# http://ofuturodascoisas.com/inovacoes-modelo-matematico-revela-os-padroes-como-elas-surgem/


#==============================================================================
#

#==============================================================================
#
#==============================================================================
np.random.seed()

n_letras=5
letras = [string.ascii_uppercase[i] for i in range(n_letras)]

r=1
U=[]
renda={}
for i in range(n_letras):
    l=letras[n_letras-i-1]
    U += [l]*r
    renda[l] = (i+1)

N=3
for i in range(100000):
    k=np.random.choice(len(U))
    U+=[U[k]]*N
    #U+=[U[k]]*renda[U[k]]


c,y=np.unique(U, return_counts=True)
a = dict(zip(c,y))

z=1.0*y/len(U)
arg = np.argsort(z)
arg = arg[::-1]

x=np.array(range(len(z)))
pl.bar(c[arg],z[arg])
pl.bar(x,z[arg])
pl.xticks(x,c[arg])
pl.xlabel(r'Posição'); pl.ylabel(r'Frequência'); 
pl.show()


pl.semilogx(x,z[arg], c='r', lw=3)
pl.show()

cc=np.polyfit(x=x, y=np.log(z[arg]), deg=1); p=np.poly1d(cc)
pl.plot(x,np.log(z[arg]),'r', x,p(x), 'b')
pl.show()

print(p)
#==============================================================================
#
#==============================================================================
