"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

# Versão Luiz Otávio
nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

# Versão Marchini
nome = 'ROBERTO'
tamanho_nome = len(nome)
contator = 0
nome_final = ''
while contator <= (tamanho_nome -1):
    letra = nome[contator] + '*'
    nome_final = nome_final + letra
    contator += 1

print(nome_final)
