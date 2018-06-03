#!/usr/bin/python
# encoding: utf-8
import numpy as np
import pylab as pl
import scipy.integrate

# escolha do parametro beta
def analisa_exponencial():
  
  n=int(1e5)
  
  pl.subplot(221)
  beta=0.5
  x=np.random.exponential(beta, n)
  pl.hist(x, 50, normed=0, facecolor='green', alpha=0.75)
  pl.title(r'$\mathrm{Dist. exponencial:}\ \beta=$%s'%beta)
  
  pl.subplot(222)
  beta=0.2
  x=np.random.exponential(beta, n)
  pl.hist(x, 50, normed=0, facecolor='green', alpha=0.75)
  pl.title(r'$\mathrm{Dist. exponencial:}\ \beta=$%s'%beta)
  pl.subplot(223)
  
  beta=0.1
  x=np.random.exponential(beta, n)
  pl.hist(x, 50, normed=0, facecolor='green', alpha=0.75)
  pl.title(r'$\mathrm{Dist. exponencial:}\ \beta=$%s'%beta)
  pl.subplot(224)
  
  beta=0.05
  x=np.random.exponential(beta, n)
  pl.hist(x, 50, normed=0, facecolor='green', alpha=0.75)
  pl.title(r'$\mathrm{Dist. exponencial:}\ \beta=$%s'%beta)
  pl.show();
  
  
def fun(x):
  return (x**10)
  
def cosxx(x):
  return np.cos(x)/x
    
def plota_funcao():
  x=np.linspace(0,1,num=100)
  pl.plot(x,fun(x))
  pl.title(r'$f(x)=x^{10}-1$')
  pl.show()
  

def montecarlo(flag, a,b,M,f,nsamples):

  if nsamples<1e7:
    nsamples=int(1e7)
  
  beta=0.09
  
  if flag==0:
    x=np.random.uniform(a,b,nsamples);
    y=np.random.uniform(0,M,nsamples);
    print ('\nMonte Carlo convencional: geração dos números aleatórios: x(uniforme), y(uniforme) \n')
    
  if flag==1:
    x=1-np.random.exponential(beta,nsamples); x[np.where(x<0)]=0
    y=np.random.uniform(0,M,nsamples);
    print ('\nMonte Carlo convencional: geração dos números aleatórios: x(exponencial), y(uniforme) \n')
  
  if flag==2:
    x=1-np.random.exponential(beta,nsamples); x[np.where(x<0)]=0
    y=np.random.exponential(beta,nsamples); y[np.where(y>M)]=M
    print ('\nMonte Carlo convencional: geração dos números aleatórios: x(exponencial), y(exponencial) \n')
  
  
  result, error = scipy.integrate.quad(f, a, b)
  yy=f(x)
  for i in range(7):
    k    = 10**i
    area = M*(b-a)*(sum(y[:k]<yy[:k])/(1.0*k))
    print (" %9d\t %f\t %f" %(k, area, result))
    
    
if __name__ == "__main__":
  
  analisa_exponencial();
  plota_funcao();
  
  a=0
  b=1
  M=1
  nsamples=1e2
  montecarlo(0,a,b,M,fun,nsamples)  
  montecarlo(1,a,b,M,fun,nsamples)
  montecarlo(2,a,b,M,fun,nsamples)
  
