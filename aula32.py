"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# minha versão
numero = input('Digite um número inteiro: ')

# teste se o número é inteiro

if "." in numero:
    print(f'{numero} não é um inteiro')
else:
    numero_inteiro = int(numero)
    if (numero_inteiro % 2) == 0:
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')

# versão do Otávio Luiz
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = "par"

    print(f'O número {entrada} é {par_impar_texto}')
else:
    print('Vovê não digitou um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = input('Digite a hora: ')

horas_inteiro = int(horas)

if horas_inteiro < 12:
    print(f'Bom dia {horas_inteiro}')
elif horas_inteiro >= 17 and horas_inteiro <= 24:
    print(f'Boa noite {horas_inteiro}')
else:
    print(f'Boa tarde {horas_inteiro}')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) > 6:
    print('Seu nome é grande')
else:
    print('Seu nome é normal')