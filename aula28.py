"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
# entrada de dados
nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

# verifica se foi digitado dados em ambas as variáveis
if nome and idade:
    print("Seu nome é", nome)
    print("Seu nome invertido é", nome[::-1])

    # verifica se há espaço vazio na variável nome
    if " " in nome:
        print("seu nome contém espaços")
    else:
        print("seu nome não contém espaços")
        
    # conta quantos caracteres tem a variável nome
    print(f"seu nome tem {len(nome)} letras")

    # mostra a primeira letra da variável nome
    print(f"A primeira letra do seu nome é {nome[0]}")

    # mostra a última letra da variável nome
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")


