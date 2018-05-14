# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:51:52 2018

@author: user
"""

import numpy as np
import pylab as pl

from scipy.misc import derivative


def f(x,r):
    return r*x*(1.-x)
    
pl.close('all')

# 0 <= r <= 4
r_vec = np.linspace(0.1, 4, 11)
x = np.linspace(-1.5,1.5,201)

for k,r in enumerate(r_vec):
    
    pl.figure(k)
    
    y = f(x,r)
        
    pl.plot(x,y,'-', label='$r = '+str(r)+'$')
    
    lambda_0 = derivative(func=f,x0= 0       , args=(r,))
    lambda_1 = derivative(func=f,x0= (r-1.)/r, args=(r,))
    
    c_0 = 'k' if abs(lambda_0)<1 else 'w'
    c_1 = 'k' if abs(lambda_1)<1 else 'w'
    
    pl.plot(x,x, 'k-')
    pl.plot(       0,       0, 'o', c=c_0)
    pl.plot((r-1.)/r,(r-1.)/r, 'o', c=c_1)
    #pl.xlim([0,1])
    pl.grid()
    pl.legend()

    pl.show() 
