#eq2grau.py
from math import sqrt
#declaração e atribuição de conteúdos de variáveis
a=-1.;b=88550000.;c=1.;
y1=(-b+sqrt(b*b-4*a*c))/(2*a)
y2=(-b-sqrt(b*b-4*a*c))/(2*a)

y1a=2*c/(-b-sqrt(b*b-4*a*c))
y2a=2*c/(-b+sqrt(b*b-4*a*c))
#impressão dos resultados
print('Raiz 1 standard=',y1,'Raiz 1 Alternativa=',y1a)
#impressão dos resultados
print('Raiz 2 standard=',y2,' Raiz 2 Alternativa=',y2a)