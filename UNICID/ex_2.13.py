import numpy as np

m = np.array([[1, 2, 3],[2, 3, 4],[4, 5, 6]])

print("Impressão da matriz quadrada:\n", m)
w, v = np.linalg.eig(m)
print("Impressão dos autovalores da matriz quadrada:\n", w)

print("Impressão dos autovetores da matriz quadrada:\n", v)