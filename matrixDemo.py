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
    u21 = 1/a**2;
    u22 = -2/a**2;
    u23 = 1/a**2;

    for j in range(N):
        for i in range(j - 1, j + 2):
            n = j+1;
            u11 = -1./2*n*(a**2);
            u13 = 1./2*n*(a**2);
            u02 = ((l**2)/(n*a)**2 - (1./(4*(n*a)**2))) + log(n*a);
            
            #print(j);
            if i == (j -1) and i >= 0 :
                #Matrix[j][i] = 1./(a**2) - 1./((j+1)*(a**2));
                Matrix[j][i] = u21 + u11;
            elif i == j:
                #Matrix[j][i] = (-2./a**2) + 1./((j+1)*a**2) - log(a/rho0, 10) - (l**2)/(((j+1)*a)**2);
                Matrix[j][i] = u22 + u02;
            elif i == (j + 1) and i < N :
                #Matrix[j][i] = 1./(a**2);
                Matrix[j][i] = u23 + u13;
    #print(Matrix); #look the matrix
    return Matrix;
#operator = Operator_generator(10000, 0, 0.250); #test result
#print(operator);

    