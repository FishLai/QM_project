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
    A21 = 1./a**2;
    A22 = -2./a**2;
    A23 = 1/a**2;
    for j in range(N):
        for i in range(j - 1, j + 2):
            n = j+1;
            A11 = -1./(n*(a**2));
            A12 = 1./(n*(a**2));
            A13 = 0;
            A01 = 0;
            A02 = -log(n*a)-(l**2)/((n*a)**2);
            A03 = 0;
            if i == (j -1) and i >= 0 :
                Matrix[j][i] = A21 + A11 + A01;#1./(a**2) - 1./((j+1)*(a**2));
            elif i == j:
                Matrix[j][i] = A22 +A12 +A02;#(-2./a**2) + 1./((j+1)*a**2) - log((j+1)*a, 10) - (l**2)/(((j+1)*a)**2);
            elif i == (j + 1) and i < N :
                Matrix[j][i] = A23 +A13 +A03;#1./(a**2);
    print(Matrix); #look the matrix
    return Matrix;
# Operator_generator(5, 0, 0.5); #test result
