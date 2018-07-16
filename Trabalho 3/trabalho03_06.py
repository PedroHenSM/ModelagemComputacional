import numpy as np
import matplotlib.pyplot as pl
import string
import operator

np.random.seed(1)
r = 1 # Quantidade inicial de letras no inicio da urna
numEventos = 10000


#N = [5,10,20,25] # Numeros de letras
#K = [2,5,10,15] # Numero de copias

N = [5]
K = [2]


# Preenche urna U com o numero 'r' de cada letra
for a in range(len(N)):
    for b in range (len(K)):
        numLetras = N[a] # Cores serão representadas por letras
        letras = [string.ascii_uppercase[i] for i in range(numLetras)]
        k = K[b] # Numero de copias da bola que será retirada
        U = [] # Urna
        qtdInovacoes = 1 # Inovacoes que serão geradas (novas cores que serão geradas)
        escolhidos = []
        for i in range(numLetras): # Preenche urna
            #l = letras[nLetras-i-1]
            l = letras[i]
            U += [l]*r

        for i in range(numEventos):
            idxEscolhido = np.random.choice(len(U))
            if(not(U[idxEscolhido] in escolhidos)): # Verifica se a letra já foi escolhida
                U += [U[idxEscolhido] + ("%d"%i) for i in range(qtdInovacoes)] # Adiciona novas letras a Urna
                escolhidos.append(U[idxEscolhido]) # Adiciona a escolhidos a letra escolhida
            U += [U[idxEscolhido]]*k # Cria k copias da letra e adiciona a urna
            
        tipoLetra,qtd = np.unique(U, return_counts = True)
        L = dict(zip(tipoLetra,qtd)) # Dicionário com letras e quantidade
        print(L)
        print(len(U))
        z = 1.0*qtd/len(U) # Vetor com a porcentagem de cada letra ao fim da urna
        arg = np.argsort(z) # Returns the indices that would sort an array.
        arg = arg[::-1] # Inverte a ordem do vetor arg
        
        print(sorted(L.items(), key=operator.itemgetter(1),reverse=True)) # Imprime dicionario
        x = np.array(range(len(z)))
        pl.bar(tipoLetra[arg],z[arg])
        pl.xticks(x,tipoLetra[arg], rotation='vertical') # Coloca as letras no eixo X ( o nome) | Apenas estética
        pl.title("Porcentagem de letras ao fim do experimento: N: {} k:{}".format(numLetras,k))
        pl.xlabel('Letras')
        pl.ylabel('Frequência')
        pl.show()
        
        cc=np.polyfit(x=x,y=np.log(z[arg]),deg=1) # "Cria" polinomio de grau 1
        p = np.poly1d(cc) # Converte 'cc' para uma reta do tipo y=ax+b
        legendas = []
        pl.title("Logaritmico e Polinomio ajustado: N: {} k:{}".format(numLetras,k))
        pl.plot(x,np.log(z[arg]),'r',label ="Logaritmica") 
        pl.plot(x,p(x),'b',label = "Polinomio Ajustado")
        pl.legend()
        pl.show()
        print(p)
        print(p[1]) # Coeficiente angular da reta y=ax+b

