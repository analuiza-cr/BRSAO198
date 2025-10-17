'''Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.'''

import random
import string

def gerar_senha_segura(comprimento):
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    
    if comprimento < 4:
        print("A senha deve ter pelo menos 4 caracteres para ser segura.")
        return None
    
   
    garantias = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    
    caracteres_restantes = [random.choice(caracteres) for _ in range(comprimento - len(garantias))]
    
    
    senha_lista = garantias + caracteres_restantes
    
    
    random.shuffle(senha_lista)
    
    
    senha_final = "".join(senha_lista)
    return senha_final


while True:
    try:
        tamanho = int(input("Digite o comprimento desejado para a senha (ex: 12): "))
        if tamanho >= 4:
            break
        else:
            print("Por favor, digite um número inteiro maior ou igual a 4.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")


senha_gerada = gerar_senha_segura(tamanho)


if senha_gerada:
    print(f"\nSua nova senha segura é: {senha_gerada}")