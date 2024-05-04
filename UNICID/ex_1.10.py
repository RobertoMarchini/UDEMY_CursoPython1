import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi,35) # 35 valores entre −pi e pi
y_sen = np.sin(x) # array senos dos valores de x
y_cos = np.cos(x) # array cos senos dos valores de x
plt.plot (x,y_sen, label = 'seno ')
plt.plot (x, y_cos , label= ' cosseno ' )
plt.xlim(-np.pi , np.pi )
plt.xlabel ( 'Ângulo [ rad ] ')
plt.ylabel ( ' Função trigonométrica ( x ) ' )
plt.grid( True )
plt.legend ( )
plt.show ( ) # mostra o gráfico
f= "a) "
print ( f, " x = { x }" )
f= "b) "
print ( f, " y_sen = { y_sen } " )
f= "c) "
print ( f, " y_cos = { y_cos } " )