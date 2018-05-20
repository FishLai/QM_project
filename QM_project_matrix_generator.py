# -*- coding: utf-8 -*-
"""
Created on Wed May 16 21:54:14 2018

@author: quan_
"""

import numpy as np;
from math import log;
"""
    create N*N zeros matrix first
"""
N = 10; #set up size of matrix
row = [0.00000]*N; 
for j in range(N):
    row[j] = [0.00000]*N; #create each element
print(row) #check zero matrix is generated
"""
    defined our hamition matrix
"""
l = 2; #use l=2 state construct matrix
a = 1; #the interval on variable axies
Omega = 1; #temperature omega value
rho0 = 1; #temperature rho0 value
for j in range(N):
    for i in range(j, j+3):
        #print(j);
        if i == j :
            row[j][i] = 1/(a**2) - 1/((j+1)*(a**2));
        elif i == (j+1) and i < N :
            row[j][i] = (-2/a**2) + 1/((j+1)*a**2) - Omega*log(a/rho0, 10) - (l**2)/(((j+1)*a)**2);
        elif i == (j+2) and i < N :
            row[j][i] = 1/(a**2);
                
print(row); #look the matrix
