nome = 'Roberto Marchini'
altura = 1.72
peso = 98
imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

# formatação de string; f-strings

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f"pesa {peso:.1f} Kg e o seu imc é {imc:.2f}"
print(linha_1)
print(linha_2)