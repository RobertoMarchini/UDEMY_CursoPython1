"""
Cálculo do centro de gravidade de uma placa semi-circular
Integrando pelo método do trapézio
"""
import numpy as np
from math import pi
import matplotlib.pyplot as plt
plt.close('all')

ro=3.5
R=50
kp=0
dx=1
for n in [11,101,1001,10001,100001,1000001]:
    x=np.linspace(-50.,50.,n)
    f=np.sqrt(R**2-x**2)
    y=f/2
    kp=kp+1
    plt.subplot(2,3,kp)
    plt.plot(x,f)
    massa=ro*(f[0]+f[n-1])/2
    xcm=ro*(f[0]*x[0]+f[n-1]*x[n-1])/2
    ycm=ro*(f[0]*y[0]+f[n-1]*y[n-1])/2
    for k in range(1,n):
        massa=massa+ro*f[k]
        xcm=xcm+ro*f[k]*x[k]
        ycm=ycm+ro*f[k]*y[k]
    massa=massa*dx
    xcm=xcm*dx/massa
    ycm=ycm*dx/massa
    print('n=%6i massa=%10.3f kg xcm=%10.3f m ycm=%12.8f m\n'   % (n,massa,xcm,ycm))
    plt.scatter(xcm,ycm)
    plt.text(xcm+5*dx,ycm,'y=%8.5f \n n=%8i' % (ycm,n))