"""
Lei do arrefecimento de Newton
Resolve a equação DT/dt=-alpha*(T-Tar), pelo método de Euler
"""
import numpy as np
import matplotlib.pyplot as plt

Tar=20 #Temperatura do ar
Tinicial=80 #Temperatura inicial do corpo
alpha=0.1 # Coeficiente de transferência de calor
#dt=0.1 #Passo de tempo
kc=0
cores=['red','blue','cyan']
plt.close('all')
for dt in[0.1,2,5]:
    tempo=np.arange(0.,120.,dt)
    n=len(tempo)
    T=np.zeros(tempo.shape)
    k=0 #Indice dos vectores
    T[k]=Tinicial
    for k in range(1,n):
        T[k]=T[k-1]-alpha*(T[k-1]-Tar)*dt
plt.plot(tempo,T,color=cores[kc])
plt.xlabel('Time (min)')
plt.ylabel(r'$T ^{o} C$') # Notar símbolo
plt.text(60,60-kc*5,r'$Euler \Delta t=%6.3f$' %(dt),color=cores[kc])

tempoAn=np.arange(0.,120.,5)
Tan=Tar+(Tinicial-Tar)*np.exp(-alpha*tempoAn)
plt.scatter(tempoAn,Tan,color='red')
kc=kc+1