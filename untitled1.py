# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:31:28 2018

@author: user
"""

import numpy as np
import pylab as pl

lamb_list = [0.6, 1.01, -0.98, -1.005]

pl.figure(1)
for lamb in lamb_list:
    
    y=[10]    

    for k in range(1,50):
        y.append(lamb**k*y[0])
            
    pl.plot(y, label='$\lambda$ = '+str(lamb))
    pl.ylabel('$y_k$')
    pl.xlabel('$k$')
    pl.grid()
    pl.legend()

pl.show()    