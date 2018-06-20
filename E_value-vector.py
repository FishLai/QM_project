# -*- coding: utf-8 -*-
"""
Spyder Editor

generate by FishLai 
"""

from matrixDemo import Operator_generator as OG;
import numpy as np;
from numpy import linalg as LA;
import matplotlib.pyplot as plt;

N = 100
Matrix = OG(N, 0, 0.004); #OG(upLimit, quantumNum, interval)

E_value, E_vector = LA.eigh(Matrix);
#print(Matrix);
#print(E_value);
#print(E_vector);

x = np.array([0]*N, dtype=np.float32);
for i in range (N):
    x[i] = (i+1)*0.004;

plt.plot(x, E_vector[0]);
plt.show();

