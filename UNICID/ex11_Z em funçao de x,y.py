import matplotlib.pyplot as plt
import numpy as np

X = np.arange (-np.pi, np.pi, 0.5)
Y = np.arange (-np.pi , np.pi, 0.5)

# Plano b i d ime n s i o n a l
X , Y = np.meshgrid( X , Y )
f_xy = np.sqrt( X ** 2 + Y ** 2)
# Plano t r i d ime n s i o n a l
Z = np.cos( f_xy )
fig,ax = plt.subplots(subplot_kw={"projection": '3d' } )
ax.plot_surface(X,Y,Z,cmap='cool') # plotagem da superfície 3D
plt.show ( )