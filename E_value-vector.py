# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:21:05 2018

@author: quan_
"""

from QM_project_matrix_generator import Operator_generator as OG;
import numpy.linalg as LA; 
import matplotlib.pyplot as plt;
import numpy as np;

N = 1000;
a = 0.001;
Matrix = OG(N, 0, a); #three parameter about number of points, quantum number and intervial
Evalue, Evector = LA.eigh(Matrix, UPLO='L');
#print(Evalue);
#print(Evector);
"""
create x axies;
"""
x = np.array([0]*N, dtype=float);
for i in range(N):
    x[i] = (i+1)*a;    
#print(Evector[0]);
"""
plot wave function;
"""
plt.plot(x, Evector[0]);
plt.show();
