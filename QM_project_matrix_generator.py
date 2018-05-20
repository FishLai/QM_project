# -*- coding: utf-8 -*-
"""
Created on Wed May 16 21:54:14 2018

@author: quan_
"""

import numpy as np;
""" create N*N zeros matrix first """
N = 10;
row = [0]*N;
for j in range(N):
    row[j] = [0]*N;
""" defined our hamition matrix """
for j in range(10):
    for i in range(10):
        row[j][i] = j*i;
print(row);
