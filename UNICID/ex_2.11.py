from sympy import Matrix
from sympy.abc import x, y
from numpy import linalg as LA
import numpy as np

A = Matrix([[4,1,0],[0,2,1],[0,0,3]])
p= A.charpoly(x).as_expr()
p

A = np.array([[4,1,0],[0,2,1],[0,0,3]])
autos = LA.eig(A)

print("Impressão dos autovalores da matriz quadrada:\n", autos[0])

print(autos[1]) #autovetor deve ser lido em coluna