'''Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.'''

# Verificador de Ano Bissexto

try:
    # Solicita o ano do usuário
    ano_str = input("Digite um ano: ")
    ano = int(ano_str)  # Converte para inteiro
    
    # Verifica se é um ano bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
    
except ValueError:
    print("Erro: Por favor, digite um valor numérico válido para o ano.")
