# -*- coding: utf-8 -*-
"""
Created on Wed May 16 21:54:14 2018
@author: quan_
"""

import numpy as np;
from math import log;


def Operator_generator(upLimit, quantumNum, interval):
    """
        create N*N zeros matrix first
    """
    N = upLimit; #set up size of matrix
    Matrix = np.zeros((N, N), dtype=np.float32);
    #print(Matrix) #check zero matrix is generated
    """
        defined our hamition matrix
    """
    l = quantumNum; #use l=2 state construct matrix
    a = interval; #the interval on variable axies
    Omega = 1.; #temperature omega value
    rho0 = 1.; #temperature rho0 value
    for j in range(N):
        for i in range(j - 1, j + 2):
            #print(j);
            if i == (j -1) and i >= 0 :
                Matrix[j][i] = 1./(a**2) - 1./((j+1)*(a**2));
            elif i == j:
                Matrix[j][i] = (-2./a**2) + 1./((j+1)*a**2) - Omega*log(a/rho0, 10) - (l**2)/(((j+1)*a)**2);
            elif i == (j + 1) and i < N :
                Matrix[j][i] = 1./(a**2);
    print(Matrix); #look the matrix
    return;
# Operator_generator(5, 0, 0.5); #test result
