import numpy as np
import matplotlib.pyplot as plt

nu=1e12*np.array([749,724,699,674,649,624,599,574,549,524,499], dtype=float)
Vp=np.array([1,0.99,0.89,0.79,0.68,0.57,0.47,0.37,0.28,0.17,0.07])

e=1.609e-19 #carga do eletron

eVp=e*Vp
Sxx=0;Sxy=0
N=len(nu)
for k in range(N):
    Sxy=Sxy+nu[k]*eVp[k]
    Sxx=Sxx+nu[k]*nu[k]
Sx=np.sum(nu)
Sy=np.sum(eVp)

a=(Sxy-Sx*Sy/N)/(Sxx-Sx**2/N)
b=(Sy-a*Sx)/N
h=a
W=-b

plt.close('all')
plt.scatter(nu,Vp)
fit=(h*nu-W)/e;
plt.plot(nu,fit)
plt.text(6.5e14,0.4,'h='+str(h))
plt.xlabel(r'$\nu$')
plt.ylabel(r'$V_p$')
plt.title('Determinação da constante de Planck')