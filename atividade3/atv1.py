'''Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).'''

# Classificador de Idade

# Solicita a idade do usuário
idade_str = input("Digite sua idade: ")  # Pede para o usuário digitar a idae
try:
    idade = int(idade_str)  # Converte a entrada para um número inteiro
    
    # Classificação da idade
    if idade >= 0 and idade <= 12:
        categoria = "Criança"
    elif idade >= 13 and idade <= 17:
        categoria = "Adolescente"
    elif idade >= 18 and idade <= 59:
        categoria = "Adulto"
    else:  
        categoria = "Idoso"
    
    # Resultado
    print(f"Você é um(a) {categoria}.")
    
except ValueError:
    print("Erro: Por favor, digite um número válido para a idade.")
