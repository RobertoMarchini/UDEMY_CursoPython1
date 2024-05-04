"""
Movimento balístico calculado pelo método de Euler
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import pi

plt.close('all')
g=9.8065
Omega=7.292e-5;phi=40;
f=2*Omega*np.sin(phi*pi/180);fP=2*Omega*np.cos(phi*pi/180)
x0=0;y0=0;z0=0 #posição inicial
u0=0;v0=0;w0=320 #velocidade inicial
timeInt=1000 #tempo máximo de integração
fig=plt.figure(1) #cria figura 1
ax=fig.add_subplot(111, projection='3d') #cria figura 3D
Cores=['blue','green','red']
kc=-1 #contador para os gráficos
for dt in[0.1,1,10]:
    kc=kc+1
    n=round(timeInt/dt) #número de passos de tempo
    tempo=np.arange(0.,timeInt,dt)
    X=np.zeros((n),dtype='float')*float('nan') #inicia com “not a number”
    Y=np.copy(X)
    Z=np.copy(X)
    U=np.copy(X)
    V=np.copy(X)
    W=np.copy(X)
    X[0]=x0
    Y[0]=y0
    Z[0]=z0
    u=u0;v=v0;w=w0;
    uP=u;vP=v;wP=w
for kt in range(1,n):
    uP=u+f*v*dt-fP*w*dt
    vP=v-f*u*dt
    wP=w+fP*u*dt-g*dt
    X[kt]=X[kt-1]+u*dt
    Y[kt]=Y[kt-1]+v*dt
    Z[kt]=Z[kt-1]+w*dt
    u=uP
    v=vP
    w=wP
    if Z[kt]<=0: #atingiu o solo!
        Z[kt]=float('nan')
        break
fig=plt.figure(1) #figura trajetoria 3D
ax.scatter(x0,y0,z0,color='red')
ax.plot(xs=X,ys=Y,zs=Z,color='cores'[kc],label=r'$\Delta t=%6.2f s $'%(dt)) #notar color e label para a legenda
Axes3D.view_init(ax,elev=30,azim=-145)
plt.xlabel('x');plt.ylabel('y')
plt.title(r'$Trajetória @\varphi=40N $')