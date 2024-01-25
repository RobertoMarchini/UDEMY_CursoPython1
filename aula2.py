'''
CRLF (carriage return + line feed) é o nome e formado do windows para a quebra de linha
\r\n (\r - return, \n - line feed ); no W11 para a quebra de linha precisa somente do \n
para UNIX somente \n
'''
print(12, 34, sep="-", end='\r\n')
print(56, 78, sep="-", end='##')
print(9, 10, sep="-", end='##\n')
print(9, 10, sep="-", end='\n##')

# A linguagem Python diferencia letras maiúsculas de minúsculas.

