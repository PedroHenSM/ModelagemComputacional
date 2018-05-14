#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:25:14 2018

@author: pedrohen
"""

import unumpy as np
import pylab as pl

ma,mb,me

ma = 0.9*ma + 0.025*me + 0.075*mb
mb = 0.8*mb + 0.05*me + 0.15*ma
me = 0.5*me + 0.25*mb + 0.25*ma
