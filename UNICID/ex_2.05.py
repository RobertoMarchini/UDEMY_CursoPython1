from sympy import Matrix
from sympy.abc import x, y

A = Matrix([[4,1,0],[0,2,1],[0,0,3]])
p= A.charpoly(x).as_expr()
p
